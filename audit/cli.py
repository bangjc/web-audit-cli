import argparse

from audit.banner import show_banner


def main():
    parser = argparse.ArgumentParser(
        description="Website Security Audit CLI"
    )

    parser.add_argument(
        "target",
        help="Target domain or URL"
    )

    args = parser.parse_args()

    show_banner()

    print(f"Target : {args.target}")