import random

def get_numbers_ticket(min, max, quantity):
    # перевірка коректності параметрів
    if min < 1 or max > 1000 or min >= max or quantity > (max - min + 1):
        return []

    numbers = set()

    # генерація унікальних випадкових чисел
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    # повертаємо відсортований список
    return sorted(numbers)
# Перевірка роботи
print(get_numbers_ticket(1, 49, 6))
