from datetime import datetime, timedelta


def get_upcoming_birthdays(
    users: list[dict[str, str]]
) -> list[dict[str, str]]:
    """
    Повертає список колег, яких потрібно привітати протягом наступних 7 днів включно.

    Вхідні дані:
    - users: список словників з ключами:
        - name: ім'я (str)
        - birthday: дата народження у форматі 'YYYY.MM.DD' (str)

    Вихідні дані:
    - список словників з ключами:
        - name (str)
        - congratulation_date: дата привітання у форматі 'YYYY.MM.DD' (str)

    Якщо день народження припадає на суботу або неділю — привітання переноситься
    на найближчий понеділок.
    """
    today = datetime.today().date()
    upcoming: list[dict[str, str]] = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until = (birthday_this_year - today).days

        if 0 <= days_until <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:  # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # неділя
                congratulation_date += timedelta(days=1)

            upcoming.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return upcoming


if __name__ == "__main__":
    users_test = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
    ]

    print(get_upcoming_birthdays(users_test))
