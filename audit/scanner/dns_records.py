import dns.resolver

from audit.utils.printer import items, title, item


class DNSRecordScanner:

    RECORDS = [
        "A",
        "AAAA",
        "MX",
        "NS",
        "TXT"
    ]

    def __init__(self, target):
        self.target = target

    def run(self):

        title("DNS Records")

        result = {
            "success": True,
            "data": {},
            "errors": []
        }

        for record in self.RECORDS:

            try:

                answers = dns.resolver.resolve(self.target, record)

                values = []

                for answer in answers:

                    values.append(str(answer))

                result["data"][record] = values

            except Exception:

                result["data"][record] = []

        # tampilkan ke terminal

        for record in self.RECORDS:

            print()

            items(record, result["data"][record])

        return result