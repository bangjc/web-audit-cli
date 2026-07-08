import socket
from audit.utils.printer import title, item


class DNSScanner:

    def __init__(self, target):
        self.target = target

    # def run(self):
    #     print("[1/2] DNS Lookup")

    #     try:
    #         hostname = socket.getfqdn(self.target)
    #         ip = socket.gethostbyname(self.target)

    #         print(f"    Hostname : {hostname}")
    #         print(f"    IP       : {ip}")

    #     except Exception as e:
    #         print(f"    ERROR    : {e}")
    def run(self):

        title("DNS Lookup")

        try:

            hostname = socket.getfqdn(self.target)
            ip = socket.gethostbyname(self.target)

            item("Hostname", hostname)
            item("IP Address", ip)

        except Exception as e:

            item("ERROR", e)