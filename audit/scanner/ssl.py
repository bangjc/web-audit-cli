import ssl
import socket

from audit.utils.printer import title, item


class SSLScanner:

    def __init__(self, target):
        self.target = target

    def run(self):

        title("SSL Certificate")

        try:

            context = ssl.create_default_context()

            with socket.create_connection((self.target, 443), timeout=10) as sock:

                with context.wrap_socket(sock, server_hostname=self.target) as ssock:

                    cert = ssock.getpeercert()

                    issuer = cert.get("issuer", ())
                    issuer_name = "-"

                    if issuer:
                        issuer_name = ", ".join(
                            value for part in issuer for key, value in part
                        )

                    item("Issuer", issuer_name)
                    item("Valid Until", cert.get("notAfter"))
                    item("Status", "VALID")

        except Exception as e:

            item("Status", "FAILED")
            item("Error", str(e))