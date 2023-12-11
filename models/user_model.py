from utilities.helper import connection,cursor


def login(data):
    email = data.get('email')
    password = data.get('password')
    cursor.execute("""SELECT * FROM users WHERE email=%s AND password=%s""", (email, password))
    return cursor.fetchone()


def find_user_by_email(email):
    cursor.execute("""SELECT * FROM users WHERE email=%s """, email)
    return cursor.fetchone()


def get_all_furniture():
    cursor.execute("""SELECT * FROM furnitures """)
    return cursor.fetchall()


def insert_forniture(data):
    name = data.get('name')
    category = data.get('category')
    price = data.get('price')
    quantity_available = data.get('quantity_available')

    furniture_data = (name, category, price, quantity_available)
    cursor.execute("""
            INSERT INTO furnitures
            (name, category, price, quantity_available)
            VALUES (%s, %s, %s, %s)""", furniture_data)
    connection.commit()