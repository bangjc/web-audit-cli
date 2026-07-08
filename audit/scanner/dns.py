import socket
from audit.utils.printer import title, item


class DNSScanner:

    def __init__(self, target):
        self.target = target

    def run(self):

        title("DNS Lookup")

        try:

            hostname = socket.getfqdn(self.target)
            ip = socket.gethostbyname(self.target)

            item("Hostname", hostname)
            item("IP Address", ip)

        except Exception as e:

            item("ERROR", e)
        
        return {
            "success": True,
            "hostname": hostname,
            "ip": ip
        }