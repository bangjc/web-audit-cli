from audit.utils.printer import title, item


class ScoreEngine:

    def __init__(self):
        self.score = 0

    def add_dns(self, success):
        if success:
            self.score += 10

    def add_http(self, status):
        if status == 200:
            self.score += 10

    def add_ssl(self, valid):
        if valid:
            self.score += 20

    def add_security_headers(self, score):
        self.score += score * 10

    def risk_level(self):

        if self.score >= 90:
            return "LOW"

        elif self.score >= 70:
            return "MEDIUM"

        elif self.score >= 40:
            return "HIGH"

        return "CRITICAL"

    def report(self):

        title("SUMMARY")

        item("Overall Score", f"{self.score}/100")
        item("Risk Level", self.risk_level())