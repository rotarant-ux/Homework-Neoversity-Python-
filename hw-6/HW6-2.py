def get_cats_info(path: str) -> list[dict[str, str]]:
    """
    Функція читає файл з інформацією про котів
    та повертає список словників.
    """

    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                cat_id, name, age = line.split(",")

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat)

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []

    except ValueError:
        print("Помилка у форматі даних.")
        return []

    return cats


def main() -> None:
    cats_info = get_cats_info("cats.txt")
    print(cats_info)


if __name__ == "__main__":
    main()