import http.client
import time
import unittest
import urllib.error
from unittest.mock import MagicMock, patch

from scripts.ai_infra_monitor.ai_infra_monitor.fetch import HttpFetcher


def make_response(body=b"ok", status=200):
    value = MagicMock()
    value.status = status
    value.headers.get.side_effect = lambda key, default="": default
    value.read.return_value = body
    value.__enter__.return_value = value
    value.__exit__.return_value = False
    return value


class HttpFetcherTests(unittest.TestCase):
    def test_hard_deadline_returns_when_transport_thread_stalls(self):
        fetcher = HttpFetcher("test", retries=0, backoff_seconds=0)

        def stalled(*args, **kwargs):
            time.sleep(0.25)

        with patch.object(fetcher, "_fetch_once", side_effect=stalled):
            started = time.monotonic()
            with self.assertRaises(TimeoutError):
                fetcher.fetch(
                    {"url": "https://example.test", "timeout_seconds": 0.1}, {}
                )

        self.assertLess(time.monotonic() - started, 0.2)

    @patch("scripts.ai_infra_monitor.ai_infra_monitor.fetch.urllib.request.urlopen")
    def test_source_can_override_timeout_and_retry_budget(self, urlopen):
        urlopen.return_value = make_response()

        HttpFetcher("test", timeout=25, retries=2, backoff_seconds=0).fetch(
            {
                "url": "https://example.test",
                "timeout_seconds": 7,
                "fetch_retries": 0,
            },
            {},
        )

        self.assertEqual(urlopen.call_args.kwargs["timeout"], 7)
        self.assertEqual(urlopen.call_count, 1)

    @patch("scripts.ai_infra_monitor.ai_infra_monitor.fetch.time.sleep")
    @patch("scripts.ai_infra_monitor.ai_infra_monitor.fetch.urllib.request.urlopen")
    def test_retries_transient_transport_errors(self, urlopen, sleep):
        urlopen.side_effect = [
            http.client.IncompleteRead(b"partial"),
            http.client.RemoteDisconnected("closed"),
            make_response(),
        ]

        result = HttpFetcher("test", retries=2, backoff_seconds=0).fetch(
            {"url": "https://example.test"}, {}
        )

        self.assertEqual(result["body"], b"ok")
        self.assertEqual(result["attempts"], 3)
        self.assertEqual(urlopen.call_count, 3)
        self.assertEqual(sleep.call_count, 2)

    @patch("scripts.ai_infra_monitor.ai_infra_monitor.fetch.time.sleep")
    @patch("scripts.ai_infra_monitor.ai_infra_monitor.fetch.urllib.request.urlopen")
    def test_retries_rate_limit_but_not_permanent_client_error(self, urlopen, sleep):
        urlopen.side_effect = [
            urllib.error.HTTPError(
                "https://example.test", 429, "rate limited", {}, None
            ),
            make_response(),
        ]

        result = HttpFetcher("test", retries=2, backoff_seconds=0).fetch(
            {"url": "https://example.test"}, {}
        )

        self.assertEqual(result["body"], b"ok")
        self.assertEqual(urlopen.call_count, 2)
        self.assertEqual(sleep.call_count, 1)

        urlopen.reset_mock()
        urlopen.side_effect = urllib.error.HTTPError(
            "https://example.test", 404, "missing", {}, None
        )
        with self.assertRaises(urllib.error.HTTPError):
            HttpFetcher("test", retries=2, backoff_seconds=0).fetch(
                {"url": "https://example.test"}, {}
            )
        self.assertEqual(urlopen.call_count, 1)


if __name__ == "__main__":
    unittest.main()
