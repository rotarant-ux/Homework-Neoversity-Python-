def caching_fibonacci() -> callable:
    """
    Функція створює кеш для зберігання вже обчислених
    чисел Фібоначчі та повертає внутрішню функцію fibonacci.
    """

    cache: dict[int, int] = {}

    def fibonacci(n: int) -> int:
        """
        Обчислює n-те число Фібоначчі з використанням кешу.
        """

        # Якщо n менше або дорівнює 0, повертаємо 0
        if n <= 0:
            return 0

        # Якщо n дорівнює 1, повертаємо 1
        if n == 1:
            return 1

        # Якщо значення вже є у кеші, повертаємо його
        if n in cache:
            return cache[n]

        # Обчислюємо значення рекурсивно та зберігаємо у кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci


def main() -> None:
    fib = caching_fibonacci()

    print(fib(10))
    print(fib(15))


if __name__ == "__main__":
    main()