from __future__ import annotations

import http.client
import socket
import time
import urllib.error
import urllib.request


class HttpFetcher:
    def __init__(
        self,
        user_agent: str,
        timeout: int = 25,
        retries: int = 2,
        backoff_seconds: float = 1.0,
    ):
        self.user_agent = user_agent
        self.timeout = timeout
        self.retries = max(0, int(retries))
        self.backoff_seconds = max(0.0, float(backoff_seconds))

    @staticmethod
    def _retryable_http_error(error: urllib.error.HTTPError) -> bool:
        return error.code in {408, 425, 429} or 500 <= error.code < 600

    def fetch(self, source: dict, cache: dict) -> dict:
        timeout = max(1, int(source.get("timeout_seconds", self.timeout)))
        retries = max(0, int(source.get("fetch_retries", self.retries)))
        headers = {
            "User-Agent": self.user_agent,
            "Accept": "application/atom+xml, application/rss+xml, application/json, text/html;q=0.9, */*;q=0.5",
        }
        if cache.get("etag"):
            headers["If-None-Match"] = cache["etag"]
        if cache.get("last_modified"):
            headers["If-Modified-Since"] = cache["last_modified"]
        request = urllib.request.Request(source["url"], headers=headers)
        last_error = None
        for attempt in range(retries + 1):
            try:
                with urllib.request.urlopen(request, timeout=timeout) as response:
                    return {
                        "status": response.status,
                        "body": response.read(),
                        "etag": response.headers.get("ETag", ""),
                        "last_modified": response.headers.get("Last-Modified", ""),
                        "attempts": attempt + 1,
                    }
            except urllib.error.HTTPError as error:
                if error.code == 304:
                    return {
                        "status": 304,
                        "body": b"",
                        "etag": cache.get("etag", ""),
                        "last_modified": cache.get("last_modified", ""),
                        "attempts": attempt + 1,
                    }
                last_error = error
                if not self._retryable_http_error(error):
                    break
            except (
                urllib.error.URLError,
                http.client.IncompleteRead,
                http.client.RemoteDisconnected,
                socket.timeout,
                TimeoutError,
                ConnectionError,
            ) as error:
                last_error = error
            if attempt < retries:
                time.sleep(self.backoff_seconds * (attempt + 1))
        raise last_error or RuntimeError(f"failed to fetch {source['url']}")
