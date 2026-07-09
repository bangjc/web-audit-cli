import whois
from datetime import datetime, timezone

from audit.utils.printer import title, item


class WhoisScanner:

    def __init__(self, target):
        self.target = target

    def run(self):

        title("WHOIS Information")

        try:

            data = whois.whois(self.target)

            registrar = data.registrar

            creation = data.creation_date
            expiration = data.expiration_date
            updated = data.updated_date

            # Beberapa registrar mengembalikan list
            if isinstance(creation, list):
                creation = creation[0]

            if isinstance(expiration, list):
                expiration = expiration[0]

            if isinstance(updated, list):
                updated = updated[0]

            item("Registrar", registrar or "-")
            item("Created", creation or "-")
            item("Expires", expiration or "-")
            item("Updated", updated or "-")

            age = None

            if creation:
                if creation.tzinfo is None:
                    now = datetime.now()
                else:
                    now = datetime.now(creation.tzinfo)

                age_days = (now - creation).days
                age_years = age_days // 365

                item("Domain Age", f"{age_years} Years")
            else:
                item("Domain Age", "-")

            return {
                "success": True,
                "data": {
                    "registrar": registrar,
                    "created": creation,
                    "expires": expiration,
                    "updated": updated,
                    "age": age,
                },
                "errors": []
            }

        except Exception as e:

            item("ERROR", str(e))

            return {
                "success": False,
                "data": {},
                "errors": [str(e)]
            }