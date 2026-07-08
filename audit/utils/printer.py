LINE = "=" * 60
SUBLINE = "-" * 60


def title(text):
    print("\n" + SUBLINE)
    print(text)
    print(SUBLINE)


def item(key, value):
    print(f"{key:<12}: {value}")