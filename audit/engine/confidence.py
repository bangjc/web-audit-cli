from audit.engine.evidence import Evidence


class ConfidenceEngine:

    def calculate(self, evidences):

        total = 0

        result = []

        for evidence in evidences:

            total += evidence.weight

            result.append(evidence.to_dict())

        return {
            "confidence": min(total, 100),
            "evidence": result
        }