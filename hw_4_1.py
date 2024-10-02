def total_salary(path):
    salaries = []
    total_salary = 0  # Змінна для загальної суми зарплати
    count_dev = 0  # Лічильник кількості розробників

    try:
        with open (path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    salary = int(salary)  # Перетворюємо зарплату у число
                    salaries.append((name, int(salary)))  # Додаємо кортеж з ім'ям і зарплатою
                    total_salary += salary  # Додаємо зарплату до загальної суми
                    count_dev += 1  # Збільшуємо лічильник кількості розробників
                except ValueError:
                    print(f"Невірний формат рядка: {line.strip()}")  # Обробка помилок форматування
        if count_dev == 0:  # Якщо немає записів
            print("Файл не містить жодного запису про зарплати.")
            return 0, 0 

        average_salary = total_salary / count_dev  # Обчислюємо середню зарплату
        return total_salary, average_salary 

    except FileNotFoundError:   # обробка коли файл не існує
        print(f"Файл '{path}' не знайдено.")
        return 0, 0
    except Exception as e:  # обробка коли формат зарплати або прізвища неправильний
        print(f"Помилка: {e}")
        return 0, 0

# Приклад використання
total, average = total_salary('salaries.txt')
print(f"Загальна сума заробітної плати: {total} UAH")
print(f"Середня заробітна плата: {average:.2f} UAH")          
    



