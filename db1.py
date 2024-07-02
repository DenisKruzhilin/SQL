import sqlite3

with sqlite3.connect('lesson_2_db.db') as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS покупки_в_магазине (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        продукт VARCHAR UNIQUE,
        кол_во INTEGER,
        цена INTEGER,
        стоимость INTEGER
    )""")
    
    products = [
        ("хлеб", 1, 32, 32),
        ("булка", 2, 15, 30),
        ("кефир", 1, 70, 70),
        ("сыр", 0.2, 450, 90),
        ("шоколад", 1, 75, 75)
    ]

    cursor.executemany("INSERT INTO покупки_в_магазине (продукт, кол_во, цена, стоимость) VALUES (?, ?, ?, ?)", products)

    cursor.execute("SELECT * FROM покупки_в_магазине")
    print(cursor.fetchall())

