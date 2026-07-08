from audit.scanner.dns import DNSScanner
from audit.scanner.http import HTTPScanner


class Scanner:

    def __init__(self, target):
        self.target = target

    def run(self):

        DNSScanner(self.target).run()

        HTTPScanner(self.target).run()