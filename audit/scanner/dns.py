import socket


class DNSScanner:

    def __init__(self, target):
        self.target = target

    def run(self):
        print("[1/2] DNS Lookup")

        try:
            hostname = socket.getfqdn(self.target)
            ip = socket.gethostbyname(self.target)

            print(f"    Hostname : {hostname}")
            print(f"    IP       : {ip}")

        except Exception as e:
            print(f"    ERROR    : {e}")