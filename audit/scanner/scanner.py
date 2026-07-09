from audit.scanner.dns import DNSScanner
from audit.scanner.http import HTTPScanner
from audit.scanner.ssl import SSLScanner
from audit.scanner.security_headers import SecurityHeaderScanner
from audit.scanner.whois import WhoisScanner
from audit.scanner.dns_records import DNSRecordScanner
from audit.scanner.geoip import GeoIPScanner
    
class Scanner:

    def __init__(self, target):
        self.target = target

    def run(self):

        result = {}

        result["dns"] = DNSScanner(self.target).run()
        ip = result["dns"]["ip"]

        result["geoip"] = GeoIPScanner(ip).run()
        result["http"] = HTTPScanner(self.target).run()

        result["ssl"] = SSLScanner(self.target).run()

        result["security_headers"] = SecurityHeaderScanner(self.target).run()
        result["dns_records"] = DNSRecordScanner(self.target).run()
        result["whois"] = WhoisScanner(self.target).run()

        return result