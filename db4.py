import sqlite3

with sqlite3.connect('home_work_lesson_4.db') as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR NOT NULL
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount INTEGER NOT NULL,
        customer INTEGER NOT NULL,
        FOREIGN KEY (customer) REFERENCES customers (customer_id)
    )""")

    # while True:
    #     input_data = input('Ввод данных для таблицы customers: ')
    #     if input_data == "stop":
    #         break

    #     table_update = input_data.split()
    #     cursor.execute("INSERT INTO customers (first_name) VALUES (?)",
    #         (table_update[0],))

    # while True:
    #     input_data = input('Ввод данных для таблицы orders: ')
    #     if input_data == "stop":
    #         break

    #     table_update = input_data.split()
    #     cursor.execute("INSERT INTO orders (amount, customer) VALUES (?,?)",
    #         (table_update[0], table_update[1]))
        
    cursor.execute("SELECT * FROM customers")
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM orders")
    print(cursor.fetchall())
    cursor.execute("SELECT customer_id FROM customers JOIN orders ON customers.customer_id = orders.customer")
    print(cursor.fetchall())

# ------------------------------------------------------------------------------
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS stores(
        store_id INTEGER PRIMARY KEY AUTOINCREMENT,
        store_name VARCHAR NOT NULL,
        city VARCHAR NOT NULL,
        region VARCHAR NOT NULL    
    )""")

    # while True:
    #     input_data = input('Ввод данных для таблицы stores: ')
    #     if input_data == "stop":
    #         break

    #     table_update = input_data.split()
    #     cursor.execute("INSERT INTO stores (store_name, city, region ) VALUES (?,?,?)", table_update[:3])

    cursor.execute("SELECT * FROM stores")
    print(cursor.fetchall())

    cursor.execute("""CREATE TABLE IF NOT EXISTS sales(
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        store_id INTEGER NOT NULL,
        sale_date DATE NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (store_id) REFERENCES stores (store_id)
    )""")

    # while True:
    #     input_data = input('Ввод данных для таблицы sales: ')
    #     if input_data == "stop":
    #         break

    #     table_update = input_data.split()
    #     cursor.execute("INSERT INTO sales (product_id, store_id, sale_date, quantity) VALUES (?,?,?,?)", table_update[:4])

    cursor.execute("SELECT * FROM sales")
    print(cursor.fetchall())

    cursor.execute("""CREATE TABLE IF NOT EXISTS products(
                   product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   product_name VARCHAR NOT NULL,
                   category VARCHAR NOT NULL,
                   price DECIMAL(10, 2) NOT NULL
    )""")

    # while True:
    #     input_data = input('Ввод данных для таблицы products: ')
    #     if input_data == "stop":
    #         break

    #     table_update = input_data.split()
    #     cursor.execute("INSERT INTO products (product_name, category, price) VALUES (?,?,?)", table_update[:3])

    cursor.execute("SELECT * FROM products")
    print(cursor.fetchall())

    cursor.execute("""CREATE TABLE IF NOT EXISTS customers_i(
                   customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   customer_name VARCHAR NOT NULL,
                   age INTEGER
    )""")

    # while True:
    #     input_data = input('Ввод данных для таблицы customers_i: ')
    #     if input_data == "stop":
    #         break

    #     table_update = input_data.split()
    #     cursor.execute("INSERT INTO customers_i (customer_name, age) VALUES (?,?)", table_update[:2])

    cursor.execute("SELECT * FROM customers_i")
    print(cursor.fetchall())

    cursor.execute("""CREATE TABLE IF NOT EXISTS orders_i (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        customer_id INTEGER,
        order_date DATE NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers_i (customer_id),
        FOREIGN KEY (product_id) REFERENCES products (product_id),
        FOREIGN KEY (product_id, quantity) REFERENCES sales (product_id, quantity)
    )""")


    # while True:
    #     input_data = input('Ввод данных для таблицы orders_i: ')
    #     if input_data == "stop":
    #         break

    #     table_update = input_data.split()
    #     cursor.execute("INSERT INTO orders_i (product_id, customer_id, order_date, quantity) VALUES (?,?,?,?)", table_update[:4])

    cursor.execute("SELECT * FROM orders_i")
    print(cursor.fetchall())

    cursor.execute("SELECT stores.store_name, stores.store_id FROM stores JOIN sales ON stores.store_id = sales.store_id")
    print(cursor.fetchall())

    cursor.execute("SELECT products.product_name, products.category, orders_i.customer_id, orders_i.order_date FROM products JOIN orders_i ON products.product_id = orders_i.product_id")
    print(cursor.fetchall())

    cursor.execute("SELECT customers_i.customer_name, orders_i.order_id FROM customers_i JOIN orders_i ON customers_i.customer_id = orders_i.customer_id JOIN sales ON orders_i.product_id = sales.product_id WHERE sales.quantity > 10")
    print(cursor.fetchall())

    db.commit()