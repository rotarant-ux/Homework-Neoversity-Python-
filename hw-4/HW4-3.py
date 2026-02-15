import re


def normalize_phone(phone_number: str) -> str:
    """
        Нормалізує номер телефону:
        - видаляє всі символи, крім цифр та '+'
        - додає міжнародний код +38, якщо відсутній
        """
    # Видаляємо всі символи, крім цифр та '+'
    cleaned = re.sub(r"[^\d+]", "", phone_number)

    # Якщо номер вже починається з '+', нічого не змінюємо
    if cleaned.startswith("+"):
        return cleaned
    # Якщо номер починається з '380', додаємо тільки '+'
    if cleaned.startswith("380"):
        return "+" + cleaned
    # В інших випадках додаємо '+38'
    return "+38" + cleaned

if __name__ == "__main__":
    raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(sanitized_numbers)


