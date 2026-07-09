import argparse

from audit import detector
from audit.banner import show_banner

from audit.detector import server
from audit.scanner import technology
from audit.scanner.dns import DNSScanner
from audit.scanner.http import HTTPScanner
from audit.engine.score import ScoreEngine
from audit.detector.server import ServerDetector


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

    # DNS Scanner
    from audit.scanner.scanner import Scanner
    scanner = Scanner(args.target)
    results = scanner.run()
    scanner.run()
    
    engine = ScoreEngine()

    engine.process(results)
    engine.report()
    
    detector = ServerDetector(results["http"])
    server = detector.detect()
    print(server)
    
    from audit.utils.printer import technology
    technology(server)


if __name__ == "__main__":
    main()