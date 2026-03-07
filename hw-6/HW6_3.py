import sys
from pathlib import Path

from colorama import Fore, Style, init


def print_directory_structure(path: Path, indent: str = "") -> None:
    """
    Рекурсивно виводить структуру директорії.
    Директорії показуються одним кольором, файли — іншим.
    """
    try:
        for item in sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower())):
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}/{Style.RESET_ALL}")
                print_directory_structure(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{indent}{Fore.RED}Немає доступу до: {path}{Style.RESET_ALL}")


def main() -> None:
    """
    Отримує шлях до директорії з аргументів командного рядка
    та виводить її структуру.
    """
    init(autoreset=True)

    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python hw03.py /шлях/до/директорії{Style.RESET_ALL}")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"{Fore.RED}Помилка: шлях не існує.{Style.RESET_ALL}")
        sys.exit(1)

    if not directory_path.is_dir():
        print(f"{Fore.RED}Помилка: вказаний шлях не є директорією.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.BLUE}{directory_path.name}/{Style.RESET_ALL}")
    print_directory_structure(directory_path)


if __name__ == "__main__":
    main()