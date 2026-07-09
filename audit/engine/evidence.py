class Evidence:

    def __init__(self, name: str, weight: int):

        self.name = name

        self.weight = weight

    def to_dict(self):

        return {
            "name": self.name,
            "weight": self.weight
        }