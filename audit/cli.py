import argparse

from audit.banner import show_banner
from audit.scanner import Scanner
from audit.scanner.dns import DNSScanner
from audit.scanner.http import HTTPScanner

def main():
    parser = argparse.ArgumentParser(
        description="Website Security Audit CLI"
    )

    parser.add_argument(
        "target",
        help="Target domain"
    )

    args = parser.parse_args()

    show_banner()

    print(f"Target : {args.target}\n")

    scanner = Scanner(args.target)

    scanner.dns_lookup()
    scanner.http_request()
    dns = DNSScanner(args.target)
    dns.run()

    http = HTTPScanner(args.target)
    http.run()