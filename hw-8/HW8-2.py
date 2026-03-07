import re
from collections.abc import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Функція знаходить у тексті всі дійсні числа
    та повертає їх через генератор.
    """
    pattern = r"\b\d+\.\d+\b"

    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Функція обчислює загальну суму чисел у тексті,
    використовуючи передану функцію-генератор.
    """
    return sum(func(text))


def main() -> None:
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими "
        "надходженнями 27.45 і 324.00 доларів."
    )

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == "__main__":
    main()