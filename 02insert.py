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
    except mysql.connector.Error as err:
        print("Veritabanı bağlantı hatası:", err)

    return connection

def read_products():
    connection = connect_database("localhost", "root", "1234", "node-app")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")

    for data in cursor:
        i = 1
        limit = len(data)
        while limit > i:
            print(data[i], end = '\t')
            i += 1
        print()

    connection.close()   
    print("Veritabanı bağlantısı kapatıldı.")

def insert_product(name, price, imageUrl, description):
    connection = connect_database("localhost", "root", "1234", "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products (name, price, imageUrl, description) VALUES (%s, %s, %s, %s)"
    values = (name, price, imageUrl, description)

    cursor.execute(sql, values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata:", err)
    finally:
        connection.close()
        print("Veritabanı bağlantısı kapatıldı.")

def insert_products(list):
    connection = connect_database("localhost", "root", "1234", "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products (name, price, imageUrl, description) VALUES (%s, %s, %s, %s)"
    values = list

    cursor.executemany(sql, values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Commit hatası:", err)
    finally:
        connection.close()
        print("Veritabanı bağlantısı kapatıldı.")

list = []
while True:
    name = input("name: ")
    price = float(input("price: "))
    imageUrl = input("image Url: ")
    description = input("description: ")

    list.append((name, price, imageUrl, description))

    result = input("devam etmek istiyor musunuz? (e/h): ")
    if result == 'h':
        print("Kayıtlarınız veritabanına aktarılıyor...")
        print(list)
        insert_products(list)
        break


# insert_product(name, price, imageUrl, description)

read_products()