
def show_phone(name, contacts):
    if name in contacts:
        return contacts[name]  # Повертає номер телефону
    else:
        return "Contact not found."  # Якщо ім'я не знайдено