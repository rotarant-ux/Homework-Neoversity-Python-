from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    # Отримуємо поточну дату (без часу)
    today = datetime.today().date()

    # Список для збереження майбутніх привітань
    upcoming = []

    # Проходимо по всіх користувачах
    for user in users:
        # Перетворюємо день народження з рядка у об'єкт date
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Формуємо день народження у поточному році
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження цього року вже минув —
        # переносимо його на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Рахуємо, через скільки днів буде день народження
        days_until = (birthday_this_year - today).days

        # Перевіряємо, чи день народження у межах наступних 7 днів (включно з сьогодні)
        if 0 <= days_until <= 7:
            congratulation_date = birthday_this_year

            # Якщо день народження припадає на суботу —
            # переносимо привітання на понеділок
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)

            # Якщо день народження припадає на неділю —
            # переносимо привітання на понеділок
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            # Додаємо інформацію про користувача у список результатів
            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    # Повертаємо список користувачів з датами привітань
    return upcoming
