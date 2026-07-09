from audit.engine.confidence import ConfidenceEngine
from audit.engine.evidence import Evidence


class ServerDetector:

    def __init__(self, http_result):
        self.http = http_result

    def detect(self):

        headers = self.http.get("headers", {})

        server = headers.get("Server")

        if not server:
            return None

        evidences = [
            Evidence("Server Header", 40)
        ]

        confidence = ConfidenceEngine().calculate(evidences)

        return {
            "technology": server,
            "category": "Web Server",
            **confidence
        }