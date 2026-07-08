from audit.utils.printer import title, item


class ScoreEngine:

    def __init__(self):

        self.score = 0

        self.summary = {}

    def process(self, result):

        # DNS
        dns_ok = result["dns"]["success"]
        self.summary["DNS"] = "PASS" if dns_ok else "FAIL"

        if dns_ok:
            self.score += 10

        # HTTP
        http_ok = result["http"]["status"] == 200
        self.summary["HTTP"] = "PASS" if http_ok else "FAIL"

        if http_ok:
            self.score += 10

        # SSL
        ssl_ok = result["ssl"]["valid"]
        self.summary["SSL"] = "PASS" if ssl_ok else "FAIL"

        if ssl_ok:
            self.score += 20

        # Security Headers
        header_score = result["security_headers"]["score"]

        self.summary["Security Headers"] = f"{header_score}/6"

        self.score += header_score * 10

    def risk(self):

        if self.score >= 90:
            return "LOW"

        elif self.score >= 70:
            return "MEDIUM"

        elif self.score >= 40:
            return "HIGH"

        return "CRITICAL"

    def report(self):

        title("SUMMARY")

        for key, value in self.summary.items():
            item(key, value)

        print()

        item("Overall Score", f"{self.score}/100")

        item("Risk Level", self.risk())