def get_cats_info(path):

    cats_info = []
    items = 0

    try:
        with open (path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    id, name, age = line.strip().split(',')
                    # Створюємо словник для кожного кота
                    cat_dict = {
                        'id': id,
                        'name': name,
                        'age': int(age)
                    }
                    cats_info.append(cat_dict)
                    items += 1  # Збільшуємо лічильник записів  
                except ValueError:
                    print(f"Невірний формат рядка: {line.strip()}")  # Обробка помилок форматування
        if items == 0:  # Якщо немає записів
            print("Файл не містить жодного запису про котів")
            return [] 

    except FileNotFoundError:   # обробка коли файл не існує
        print(f"Файл '{path}' не знайдено.")
        return []
    except Exception as e:  # обробка інших помилок 
        print(f"Помилка: {e}")
        return []
    
    return cats_info  # Повертаємо список котів 


cats_info = get_cats_info('cats.txt')
for cat in cats_info:
    print(cat)