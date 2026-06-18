from __future__ import annotations

import time
import urllib.error
import urllib.request


class HttpFetcher:
    def __init__(self, user_agent: str, timeout: int = 25):
        self.user_agent = user_agent
        self.timeout = timeout

    def fetch(self, source: dict, cache: dict) -> dict:
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
        for attempt in range(3):
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    return {
                        "status": response.status,
                        "body": response.read(),
                        "etag": response.headers.get("ETag", ""),
                        "last_modified": response.headers.get("Last-Modified", ""),
                    }
            except urllib.error.HTTPError as error:
                if error.code == 304:
                    return {
                        "status": 304,
                        "body": b"",
                        "etag": cache.get("etag", ""),
                        "last_modified": cache.get("last_modified", ""),
                    }
                last_error = error
                if 400 <= error.code < 500:
                    break
            except urllib.error.URLError as error:
                last_error = error
            if attempt < 2:
                time.sleep(1 + attempt)
        raise last_error or RuntimeError(f"failed to fetch {source['url']}")
