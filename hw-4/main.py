#імпортую модуль datetime із бібліотеки datetime
from datetime import datetime

# Створюю фунцію, як вказано в ТЗ

def get_days_from_today(date):

    try: # Застосовую try/except для роботи з помилками
        check_date = datetime.strptime(date, "%Y-%m-%d") # парсинг дати в заданому форматі
        now = datetime.now().date() # фіксую поточну дату
        delta = now - check_date.date() # вираховую різницю в днях
        return delta.days # повертаю результат
    except ValueError:
        raise ValueError("Невірний формат, введіть у форматі: YYYY-MM-DD")

result = get_days_from_today("2030-01-01")
print(result)

