from audit.scanner.dns import DNSScanner
from audit.scanner.http import HTTPScanner
from audit.scanner.ssl import SSLScanner
from audit.scanner.security_headers import SecurityHeaderScanner


class Scanner:

    def __init__(self, target):
        self.target = target

    def run(self):

        result = {}

        result["dns"] = DNSScanner(self.target).run()

        result["http"] = HTTPScanner(self.target).run()

        result["ssl"] = SSLScanner(self.target).run()

        result["security_headers"] = SecurityHeaderScanner(self.target).run()

        return result