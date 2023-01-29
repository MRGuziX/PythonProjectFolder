import psycopg2

# establishing the connection
conn = psycopg2.connect(
    database="postgres", user='postgres', password='password', host='127.0.0.1', port='5432'
)
conn.autocommit = True
cursor = conn.cursor()


def create_database():
    sql_db = '''CREATE database book_title_components'''
    cursor.execute(sql_db)
    print("Database created successfully........")


def create_table():
    sql_table = '''CREATE TABLE components(
        first_part CHAR(20),
        preposition CHAR(20),
        second_part CHAR(20)
        )'''

    cursor.execute(sql_table)
    print("Table created successfully........")


def add_value_to_database():
    conn.autocommit = False
    cursor.execute("INSERT INTO components (first_part, preposition, second_part) VALUES('heroes', 'of the', "
                   "'universe')")
    print("Value added successfully........")


def check_inserts():
    cursor.execute("SELECT * FROM components")
    print(cursor.fetchall())


def delete_database():
    cursor.execute("DROP DATABASE book_title_components")


def delete_table():
    cursor.execute("DROP TABLE components")


def close_connection_and_cursor():
    cursor.close()
    conn.close()


class DatabaseCreator:

    delete_database()
    delete_table()
    create_database()
    create_table()
    add_value_to_database()
    check_inserts()
    close_connection_and_cursor()
