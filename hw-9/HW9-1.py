from collections import UserDict


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
    Виконує валідацію: номер має містити рівно 10 цифр.
    """

    def __init__(self, value: str) -> None:
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


class Record:
    """
    Клас для зберігання інформації про контакт:
    ім'я та список телефонів.
    """

    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones: list[Phone] = []

    def add_phone(self, phone: str) -> None:
        """
        Додає телефон до списку телефонів контакту.
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        """
        Видаляє телефон зі списку телефонів контакту.
        """
        phone_to_remove = self.find_phone(phone)

        if phone_to_remove:
            self.phones.remove(phone_to_remove)

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """
        Замінює старий номер телефону на новий.
        """
        phone_to_edit = self.find_phone(old_phone)

        if phone_to_edit:
            self.phones.remove(phone_to_edit)
            self.phones.append(Phone(new_phone))
        else:
            raise ValueError("Phone number not found.")

    def find_phone(self, phone: str) -> Phone | None:
        """
        Шукає телефон у списку телефонів контакту.
        """
        for contact_phone in self.phones:
            if contact_phone.value == phone:
                return contact_phone
        return None

    def __str__(self) -> str:
        return (
            f"Contact name: {self.name.value}, "
            f"phones: {'; '.join(phone.value for phone in self.phones)}"
        )


class AddressBook(UserDict):
    """
    Клас для зберігання записів та керування ними.
    """

    def add_record(self, record: Record) -> None:
        """
        Додає запис до адресної книги.
        """
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        """
        Повертає запис за ім'ям.
        """
        return self.data.get(name)

    def delete(self, name: str) -> None:
        """
        Видаляє запис за ім'ям.
        """
        if name in self.data:
            del self.data[name]


def main() -> None:
    """
    Приклад використання адресної книги.
    """
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)

    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print(john)

        found_phone = john.find_phone("5555555555")
        print(f"{john.name}: {found_phone}")

    book.delete("Jane")


if __name__ == "__main__":
    main()