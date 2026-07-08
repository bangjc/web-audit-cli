from colorama import Fore, Style, init

init(autoreset=True)


def show_banner():

    print(Fore.CYAN + "=" * 60)
    print("               WEB AUDIT CLI v0.1")
    print("          Website Security Auditor")
    print("=" * 60)
    print(Style.RESET_ALL)