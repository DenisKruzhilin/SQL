import sqlite3

with sqlite3.connect('home_work_lesson_3_db_products.db') as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS prodacts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR NOT NULL,
        count INTEGER NOT NULL,
        price FLOAT NOT NULL,
        country CHAR(2) NOT NULL
    )""")

    while True:
        input_data = input('Ввод данных товаров для б/д: ')
        if input_data == "stop":
            break

        table_uppdate = input_data.split()
        cursor.execute("INSERT INTO prodacts (name, count, price, country) VALUES (?, ?, ?, ?)",
            table_uppdate[:4])
        
    cursor.execute("SELECT * FROM prodacts")
    print(cursor.fetchall())

    cursor.execute("SELECT name FROM prodacts WHERE country = 'RU' or country = 'BL'")
    print(cursor.fetchall())

    cursor.execute("SELECT name FROM prodacts WHERE country IN ('RU','BL')")
    print(cursor.fetchall())

    cursor.execute("SELECT name FROM prodacts WHERE price >= 10000 AND price <= 20000")
    print(cursor.fetchall())
    # Условие задание о выводе через OR, вероятно неверно, т.к. при данном выводе мы получим все результаты таблицы

    cursor.execute("SELECT name FROM prodacts WHERE price BETWEEN 10000 and 20000")
    print(cursor.fetchall())

    cursor.execute("SELECT name FROM prodacts WHERE count = 0")
    print(cursor.fetchall())

    cursor.execute("SELECT price FROM prodacts WHERE country = 'US'")
    print(cursor.fetchall())

    db.commit() 