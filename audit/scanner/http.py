import time
import requests

from audit.utils.printer import title, item


class HTTPScanner:

    def __init__(self, target):
        self.target = target

    def run(self):

        title("HTTP Request")

        try:

            start = time.perf_counter()

            response = requests.get(
                f"https://{self.target}",
                timeout=10,
                allow_redirects=True,
                headers={
                    "User-Agent": "WebAuditCLI/1.0"
                }
            )

            elapsed = (time.perf_counter() - start) * 1000

            item("URL", response.url)
            item("Status", response.status_code)
            item("Server", response.headers.get("Server", "-"))
            item("Response", f"{elapsed:.2f} ms")

        except Exception as e:

            item("ERROR", e)
        
        return {
            "success": True,
            "status": response.status_code,
            "url": response.url,
            "headers": dict(response.headers),
            "html": response.text,
            "cookies": response.cookies.get_dict(),
            "server": response.headers.get("Server", "-"),
            "response_time": elapsed,
        }