import time
import requests


class HTTPScanner:

    def __init__(self, target):
        self.target = target

    def run(self):
        print("\n[2/2] HTTP Request")

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

            print(f"    URL          : {response.url}")
            print(f"    Status       : {response.status_code}")
            print(f"    Server       : {response.headers.get('Server', '-')}")
            print(f"    Response     : {elapsed:.2f} ms")

        except Exception as e:
            print(f"    ERROR        : {e}")