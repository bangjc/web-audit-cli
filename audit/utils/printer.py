LINE = "=" * 60
SUBLINE = "-" * 60


def title(text):
    print("\n" + SUBLINE)
    print(text)
    print(SUBLINE)


def item(key, value):
    print(f"{key:<12}: {value}")

def items(title, values):

    item(title, "")

    if values:
        for value in values:
            print(f"   • {value}")
    else:
        print("   • -")
        
def confidence(result):

    item("Confidence", f"{result['confidence']}%")

    print()

    print("Evidence")

    for ev in result["evidence"]:

        print(f"   ✔ {ev['name']} (+{ev['weight']})")

def technology(result):
    title("Technology Detection")

    if not result:
        item("Web Server", "Unknown")
        return

    item(result["category"], result["technology"])
    item("Confidence", f'{result["confidence"]}%')

    print("\nEvidence")

    for ev in result["evidence"]:
        print(f"   ✔ {ev['name']} (+{ev['weight']})")