import socket
import time

import requests


class Scanner:

    def __init__(self, target):
        self.target = target

    def dns_lookup(self):
        print("[1/3] DNS Lookup...")

        try:
            ip = socket.gethostbyname(self.target)
            print(f"    IP Address : {ip}")
        except Exception as e:
            print(f"    ERROR : {e}")

    def http_request(self):
        print("\n[2/3] HTTP Request...")

        try:
            start = time.perf_counter()

            response = requests.get(
                f"https://{self.target}",
                timeout=10
            )

            elapsed = (time.perf_counter() - start) * 1000

            print(f"    Status Code : {response.status_code}")
            print(f"    Response Time : {elapsed:.2f} ms")

        except Exception as e:
            print(f"    ERROR : {e}")