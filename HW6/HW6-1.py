def total_salary(path: str) -> tuple[int, float]:
    """
    Функція читає файл із зарплатами розробників.

    Кожен рядок файлу має формат:
    Ім'я Прізвище,зарплата

    Повертає кортеж:
    (загальна сума зарплат, середня зарплата)
    """

    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                name, salary = line.split(",")

                total += int(salary)
                count += 1

    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0

    except ValueError:
        print("Помилка у форматі даних.")
        return 0, 0

    if count == 0:
        return 0, 0

    average = total / count

    return total, average


def main() -> None:
    total, average = total_salary("salary.txt")

    print(
        f"Загальна сума заробітної плати: {total}, "
        f"Середня заробітна плата: {average}"
    )


if __name__ == "__main__":
    main()