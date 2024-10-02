
from hw_4_3_parse import parse_input
from hw_4_3_add_contact import add_contact
from hw_4_3_change import change_contact
from hw_4_3_show_phone import show_phone
from hw_4_3_show_all import show_all



def main():
    contacts = {}
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
            print(add_contact(args, contacts))
        elif command == "change":
            if len(args) != 2:
                print("Invalid command. Usage: change [name] [new phone number]")
            else:
                print(change_contact(args, contacts))
        elif command == "phone":
            if len(args) != 1:
                print("Invalid command. Usage: phone [name]")
            else:
                print(show_phone(args[0], contacts))
        elif command == "all":
            print(show_all(contacts))  # Викликаємо функцію show_all
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()