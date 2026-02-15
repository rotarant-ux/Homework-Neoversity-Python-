import random


def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list[int]:
    """
        Генерує відсортований список унікальних випадкових чисел у діапазоні [min_num, max_num].

        Якщо параметри не відповідають обмеженням — повертає [].
        """
    if (
        min_num < 1
        or max_num > 1000
        or min_num >= max_num
        or quantity <= 0
        or quantity > (max_num - min_num + 1)
    ):
        return []

    numbers: set[int] = set()

    while len(numbers) < quantity:
        numbers.add(random.randint(min_num, max_num))

    return sorted(numbers)

if __name__ == '__main__':
    print(get_numbers_ticket(1, 49, 6))
