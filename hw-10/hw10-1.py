from collections import UserDict
from datetime import datetime, date, timedelta


def input_error(func):
    """
    Декоратор для обробки помилок введення користувача.
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return str(error)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the required arguments for the command."

    return inner


class Field:
    """
    Базовий клас для полів запису.
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    """
    Клас для зберігання імені контакту.
    """

    pass


class Phone(Field):
    """
    Клас для зберігання номера телефону.
    Номер має складатися рівно з 10 цифр.
    """

    def __init__(self, value: str) -> None:
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


class Birthday(Field):
    """
    Клас для зберігання дня народження.
    Формат: DD.MM.YYYY
    """

    def __init__(self, value: str) -> None:
        try:
            birthday_date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

        super().__init__(value)
        self.date_value = birthday_date


class Record:
    """
    Клас для зберігання інформації про контакт:
    ім'я, список телефонів і день народження.
    """

    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None

    def add_phone(self, phone: str) -> None:
        """
        Додає телефон до контакту.
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        """
        Видаляє телефон із контакту.
        """
        phone_to_remove = self.find_phone(phone)

        if phone_to_remove:
            self.phones.remove(phone_to_remove)
        else:
            raise ValueError("Phone number not found.")

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """
        Замінює старий телефон на новий.
        """
        phone_to_edit = self.find_phone(old_phone)

        if phone_to_edit:
            self.phones.remove(phone_to_edit)
            self.phones.append(Phone(new_phone))
        else:
            raise ValueError("Phone number not found.")

    def find_phone(self, phone: str) -> Phone | None:
        """
        Шукає телефон у контакті.
        """
        for contact_phone in self.phones:
            if contact_phone.value == phone:
                return contact_phone
        return None

    def add_birthday(self, birthday: str) -> None:
        """
        Додає день народження до контакту.
        """
        self.birthday = Birthday(birthday)

    def __str__(self) -> str:
        phones_str = "; ".join(phone.value for phone in self.phones)
        birthday_str = self.birthday.value if self.birthday else "not set"
        return (
            f"Contact name: {self.name.value}, "
            f"phones: {phones_str}, "
            f"birthday: {birthday_str}"
        )


class AddressBook(UserDict):
    """
    Клас для зберігання та керування контактами.
    """

    def add_record(self, record: Record) -> None:
        """
        Додає запис до адресної книги.
        """
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        """
        Знаходить запис за ім'ям.
        """
        return self.data.get(name)

    def delete(self, name: str) -> None:
        """
        Видаляє запис за ім'ям.
        """
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError

    def get_upcoming_birthdays(self) -> list[dict[str, str]]:
        """
        Повертає список користувачів, яких потрібно
        привітати протягом наступного тижня.
        """
        today = date.today()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            birthday_this_year = record.birthday.date_value.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            days_difference = (birthday_this_year - today).days

            if 0 <= days_difference <= 7:
                congratulation_date = birthday_this_year

                if congratulation_date.weekday() >= 5:
                    days_to_monday = 7 - congratulation_date.weekday()
                    congratulation_date = congratulation_date + timedelta(days=days_to_monday)

                upcoming_birthdays.append(
                    {
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime("%d.%m.%Y"),
                    }
                )

        return upcoming_birthdays


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Розбирає введений рядок на команду та аргументи.
    """
    parts = user_input.split()

    if not parts:
        return "", []

    cmd, *args = parts
    return cmd.strip().lower(), args


@input_error
def add_contact(args: list[str], book: AddressBook) -> str:
    """
    Додає новий контакт або телефон до існуючого контакту.
    """
    name, phone, *_ = args
    record = book.find(name)

    message = "Contact updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    record.add_phone(phone)
    return message


@input_error
def change_contact(args: list[str], book: AddressBook) -> str:
    """
    Змінює телефон контакту.
    """
    name, old_phone, new_phone = args
    record = book.find(name)

    if record is None:
        raise KeyError

    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def show_phone(args: list[str], book: AddressBook) -> str:
    """
    Показує всі телефони контакту.
    """
    name = args[0]
    record = book.find(name)

    if record is None:
        raise KeyError

    return "; ".join(phone.value for phone in record.phones)


@input_error
def show_all(book: AddressBook) -> str:
    """
    Показує всі контакти адресної книги.
    """
    if not book.data:
        return "No contacts saved."

    return "\n".join(str(record) for record in book.data.values())


@input_error
def add_birthday(args: list[str], book: AddressBook) -> str:
    """
    Додає день народження контакту.
    """
    name, birthday = args
    record = book.find(name)

    if record is None:
        raise KeyError

    record.add_birthday(birthday)
    return "Birthday added."


@input_error
def show_birthday(args: list[str], book: AddressBook) -> str:
    """
    Показує день народження контакту.
    """
    name = args[0]
    record = book.find(name)

    if record is None:
        raise KeyError

    if record.birthday is None:
        return "Birthday not set."

    return record.birthday.value


@input_error
def birthdays(args: list[str], book: AddressBook) -> str:
    """
    Показує список найближчих днів народження.
    """
    upcoming_birthdays = book.get_upcoming_birthdays()

    if not upcoming_birthdays:
        return "No birthdays in the upcoming week."

    return "\n".join(
        f"{item['name']}: {item['congratulation_date']}"
        for item in upcoming_birthdays
    )


def main() -> None:
    """
    Основний цикл роботи бота.
    """
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()