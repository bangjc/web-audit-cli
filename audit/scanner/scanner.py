from audit.scanner.dns import DNSScanner
from audit.scanner.http import HTTPScanner
from audit.scanner.ssl import SSLScanner
from audit.scanner.security_headers import SecurityHeaderScanner

class Scanner:

    def __init__(self, target):
        self.target = target

    def run(self):

        DNSScanner(self.target).run()
        HTTPScanner(self.target).run()
        SSLScanner(self.target).run()
        SecurityHeaderScanner(self.target).run()