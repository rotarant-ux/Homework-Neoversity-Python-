def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.split()

    if not parts:
        return "", []

    cmd, *args = parts
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return "Contact updated."

    return "Contact not found."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    name = args[0]

    if name in contacts:
        return contacts[name]

    return "Contact not found."


def show_all(contacts: dict[str, str]) -> str:
    if not contacts:
        return "No contacts saved."

    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    contacts: dict[str, str] = {}
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
            if len(args) != 2:
                print("Invalid command.")
            else:
                print(add_contact(args, contacts))

        elif command == "change":
            if len(args) != 2:
                print("Invalid command.")
            else:
                print(change_contact(args, contacts))

        elif command == "phone":
            if len(args) != 1:
                print("Invalid command.")
            else:
                print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()