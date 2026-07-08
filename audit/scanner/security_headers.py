import requests

from audit.utils.printer import title, item


class SecurityHeaderScanner:

    SECURITY_HEADERS = {
        "Strict-Transport-Security": "HSTS",
        "Content-Security-Policy": "CSP",
        "X-Frame-Options": "X-Frame",
        "X-Content-Type-Options": "NoSniff",
        "Referrer-Policy": "Referrer",
        "Permissions-Policy": "Permissions"
    }

    def __init__(self, target):
        self.target = target

    def run(self):

        title("Security Headers")

        try:

            response = requests.get(
                f"https://{self.target}",
                timeout=30,
                allow_redirects=True,
                verify=True,
                headers={
                    "User-Agent": "WebAuditCLI/1.0"
                }
            )

            headers = response.headers

            score = 0

            for header, label in self.SECURITY_HEADERS.items():

                if header in headers:
                    item(label, "YES")
                    score += 1
                else:
                    item(label, "NO")

            print()
            item("Score", f"{score}/6")

        except Exception as e:

            item("ERROR", str(e))
        
        return {
            "score": score
        }