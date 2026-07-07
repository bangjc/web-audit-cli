from colorama import Fore, Style, init

init(autoreset=True)


def show_banner():
    print(Fore.CYAN + "=" * 50)
    print("         WEB AUDIT CLI")
    print("     Website Security Auditor")
    print("=" * 50)
    print(Style.RESET_ALL)