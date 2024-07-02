import sqlite3

with sqlite3.connect('home_work_lesson_3.db') as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR NOT NULL,
        last_name VARCHAR NOT NULL,
        birthday DATE NOT NULL,
        age INTEGER NOT NULL,
        gender CHAR(1) NOT NULL
    )""")

    while True:
        input_data = input('Ввод данных пользователя для б/д: ')
        if input_data == "stop":
            break

        table_uppdate = input_data.split()
        cursor.execute("INSERT INTO users (first_name, last_name, birthday, age, gender) VALUES (?, ?, ?, ?, ?)",
            table_uppdate[:5])
        
    # cursor.execute("DELETE FROM users") очистка б/д

    print("Данные успешно добавлены в базу данных. Список всех пользователей.")

    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())

    cursor.execute("SELECT first_name, last_name FROM users WHERE age >= 18 and gender = 'm' ")
    print(cursor.fetchall())
    cursor.execute("SELECT first_name, last_name FROM users WHERE gender = 'w' ")
    print(cursor.fetchall())

    db.commit()        