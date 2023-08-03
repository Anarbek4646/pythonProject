import sqlite3


conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL
                )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    area REAL DEFAULT 0,
                    country_id INTEGER,
                    FOREIGN KEY (country_id) REFERENCES countries(id)
                )''')


cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    city_id INTEGER,
                    FOREIGN KEY (city_id) REFERENCES cities(id)
                )''')


cursor.executemany("INSERT INTO countries (title) VALUES (?)", [("Кыргызстан",), ("Германия",), ("Китай",)])

cursor.executemany("INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)",
                   [("Бишкек", 124.0, 1), ("Ош", 75.0, 1), ("Берлин", 891.8, 2), ("Пекин", 16410.54, 3),
                    ("Москва", 2561.5, 0), ("Токио", 2187.66, 0), ("Лондон", 1572.0, 0)])

# Заполнение таблицы employees
cursor.executemany("INSERT INTO employees (first_name, last_name, city_id) VALUES (?, ?, ?)",
                   [("Иван", "Иванов", 1), ("Петр", "Петров", 2), ("Анна", "Сидорова", 3),
                    ("John", "Doe", 4), ("Jane", "Smith", 5), ("Иван", "Пупкин", 6),
                    ("Алиса", "Кошкина", 1), ("Максим", "Максимов", 2), ("Мария", "Мариева", 3),
                    ("Emily", "Johnson", 4), ("Michael", "Brown", 5), ("Екатерина", "Смирнова", 6),
                    ("Игорь", "Игорев", 1), ("Светлана", "Светланова", 2), ("Виктор", "Викторов", 3)])

conn.commit()

def display_cities():
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    print("Список городов:")
    for city in cities:
        print(f"{city[0]}. {city[1]}")

def display_employees_by_city(city_id):
    cursor.execute('''SELECT employees.first_name, employees.last_name,
                      countries.title, cities.title, cities.area
                      FROM employees
                      JOIN cities ON employees.city_id = cities.id
                      JOIN countries ON cities.country_id = countries.id
                      WHERE cities.id = ?''', (city_id,))
    employees = cursor.fetchall()
    print("Сотрудники, проживающие в выбранном городе:")
    for employee in employees:
        print(f"Имя: {employee[0]}, Фамилия: {employee[1]}, Страна: {employee[2]}, Город: {employee[3]}, Площадь города: {employee[4]}")

# Основная программа
if __name__ == "__main__":
    while True:
        print("Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
        display_cities()
        city_id = int(input("Введите id города: "))
        if city_id == 0:
            break
        display_employees_by_city(city_id)

    conn.close()