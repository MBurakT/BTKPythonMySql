import mysql.connector

def connect_database(host, user, password, database):
    try: 
        connection = mysql.connector.connect(
            host = host, 
            user = user, 
            password = password, 
            database = database
        )
        print("Veritabanı bağlantısı gerçekleştirildi.")
        return connection
    except mysql.connector.Error as err:
        print("Veritabanı bağlantı hatası:", err)
        return

def read_products():
    connection = connect_database("localhost", "root", "1234", "node-app")
    if not connection:
        return

    cursor = connection.cursor()

    cursor.execute("SHOW COLUMNS FROM products")
    cols = cursor.fetchall()

    i = 1
    limit = len(cols)
    while limit > i:
        print(str(cols[i][0]).ljust(20), end = '')
        i += 1

    print()

    cursor.execute("SELECT * FROM products")
    datas = cursor.fetchall()

    for data in datas:
        i = 1
        limit = len(data)
        while limit > i:
            print(str(data[i]).ljust(20, ' '), end = '')
            i += 1
        print()

    cursor.close()
    connection.close() 
    print("Veritabanı bağlantısı kapatıldı.")

read_products()