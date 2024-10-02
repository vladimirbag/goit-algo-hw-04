
def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid input. Usage: change [name] [new phone number]"
    
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone  # Оновлення номера телефону
        return "Contact updated."
    else:
        return "Contact not found."