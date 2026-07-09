import requests

from audit.utils.printer import title, item


class GeoIPScanner:

    def __init__(self, ip):
        self.ip = ip

    def run(self):

        title("IP Information")

        result = {
            "success": False,
            "data": {},
            "errors": []
        }

        try:

            response = requests.get(
                f"https://ipwho.is/{self.ip}",
                timeout=10
            )

            data = response.json()

            if not data.get("success", True):
                raise Exception(data.get("message", "Unknown error"))

            result["success"] = True

            result["data"] = data

            item("IP Address", data.get("ip"))

            item("Country", data.get("country"))

            item("Region", data.get("region"))

            item("City", data.get("city"))

            item("Timezone", data.get("timezone", {}).get("id"))

            item("ISP", data.get("connection", {}).get("isp"))

            item("ASN", data.get("connection", {}).get("asn"))

            item("Organization", data.get("connection", {}).get("org"))

        except Exception as e:

            item("ERROR", str(e))

            result["errors"].append(str(e))

        return result