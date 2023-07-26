import  sqlite3

def creat_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as a:
        print(a)
    return connection

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as a:
        print(a)


def insert_product(conn, products):
    sql = '''
    INSERT INTO products (product_title, price, quantity)
    VALUES (?,?,?)
    '''
    try:
        cursor = conn.cursor()
        cursor.executemany(sql, products)
        conn.commit()
    except sqlite3.Error as a:
        print(a)
def update_quantity(conn, new_quantity):
    sql = '''
        UPDATE products SET quantity = ? WHERE id = ?
        '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, new_quantity)
        conn.commit()
    except sqlite3.Error as a:
        print(a)


def update_price(conn, new_price):
    sql = '''
        UPDATE products SET quantity = ? WHERE id = ?
        '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, new_price)
        conn.commit()
    except sqlite3.Error as a:
        print(a)

def delete_product_by_id(conn, product_id):
    sql = '''
        DELETE FROM products WHERE id = ?
        '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (product_id,))
        conn.commit()
    except sqlite3.Error as a:
        print(a)

def select_all_products(conn):
    sql = '''SELECT * FROM products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        for row in rows:
            for i in row:
                print(i, end= ', ')
            print('\n')

    except sqlite3.Error as a:
        print(a)

def select_products_by_price_limit(conn, limit):
    sql = '''SELECT * FROM products
    WHERE price < ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (limit,))

        rows = cursor.fetchall()
        for row in rows:
            for i in row:
                print(i, end= ', ')
            print('\n')

    except sqlite3.Error as a:
        print(a)

def search_products_by_title(conn, keyword):
    sql = '''SELECT * FROM products
    WHERE product_title LIKE ? OR product_title LIKE ?'''

    try:
        cursor = conn.cursor()
        cursor2 = conn.cursor()
        keywordlow = '%'+keyword+'%'
        keywordupp = '%'+keyword.capitalize()+'%'

        cursor.execute(sql, (keywordupp, keywordlow))


        rows = cursor.fetchall()
        for row in rows:
            for i in row:
                print(i, end= ', ')
            print('\n')

    except sqlite3.Error as a:
        print(a)



sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title TEXT(200) NOT NULL,
price NUMERIC(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
)
'''

products_data = [
        ("Жидкое мыло с запахом ванили", 5.99, 50),
        ("Мыло детское", 3.49, 100),
        ("Шампунь для волос", 12.75, 30),
        ("Зубная паста", 2.99, 150),
        ("Крем для рук", 7.50, 80),
        ("Гель для душа", 8.25, 70),
        ("Туалетная бумага", 4.50, 200),
        ("Салфетки бумажные", 1.99, 300),
        ("Мыло для посуды", 2.25, 40),
        ("Полотенце", 6.99, 50),
        ("Кухонные перчатки", 3.75, 60),
        ("Мочалка для тела", 3.25, 40),
        ("Губки для посуды", 1.50, 100),
        ("Мыло-скраб", 4.99, 30),
        ("Бальзам для губ", 2.49, 70),
    ]



connection_to_db = creat_connection('hw.db')

if connection_to_db is not None:
    print('Successfully connected to DB!')
    #create_table(connection_to_db, sql_create_products_table)
    #insert_product(connection_to_db, products_data)

    # update_quantity(connection_to_db, (50, 2))
    # update_price(connection_to_db, (5.54, 2))
    delete_product_by_id(connection_to_db, 3)
    print('\nВсе товары из таблицы Product\n')

    select_all_products(connection_to_db)
    print('Все товары из таблицы Product цена котрых меньше 100\n')

    select_products_by_price_limit(connection_to_db, 100)

    print('товары с названием “мыло” \n')
    search_products_by_title(connection_to_db, 'мыло')
    connection_to_db.close()
