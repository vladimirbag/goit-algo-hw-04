
def show_all(contacts):
    if contacts:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()  # Видаляє зайві пробіли або нові рядки в кінці
    else:
        return "No contacts found."  # Якщо немає контактів
    
