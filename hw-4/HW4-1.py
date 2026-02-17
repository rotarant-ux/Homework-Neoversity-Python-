from datetime import datetime


def get_days_from_today(date_str: str) -> int:
    """
    Повертає кількість днів від заданої дати до поточної.

    :param date_str: Рядок у форматі 'YYYY-MM-DD'
    :return: Різниця в днях (int)
    :raises ValueError: Якщо формат дати некоректний
    """
    try:
        check_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Невірний формат, введіть у форматі: YYYY-MM-DD")
    today = datetime.today().date()
    return (today - check_date).days


if __name__ == "__main__":
    print(get_days_from_today("2027-02-16"))

