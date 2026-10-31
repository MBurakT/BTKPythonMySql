import mysql.connector

def connect_database(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host = host, 
            user = user, 
            password = password, 
            database = database
        )
        print("Veritabanı bağlantası yapıldı.".center(50))
        return connection
    except mysql.connector.Error as err:
        print("Veritabanı bağlantısı başarısız! Hata:", err)
        return 

def get_products():
    connection = connect_database(
        host = "localhost", 
        user = "root", 
        password = "1234", 
        database = "node-app"
    )
    if not connection:
        return

    mycursor = connection.cursor()

    sql = "SELECT * FROM products"

    mycursor.execute(sql)
    datas = mycursor.fetchall()

    for data in datas:
        print(data)

    mycursor.close()
    connection.close()
    print("Veritabanı bağlantısı kapatıldı.".center(50))

def update_product():
    connection = connect_database(
        host = "localhost", 
        user = "root", 
        password = "1234", 
        database = "node-app"
    )
    if not connection:
        return

    mycursor = connection.cursor()

    sql = "UPDATE products SET name = 'Samsung S10', price = 5000 WHERE id = 1"

    try:
        mycursor.execute(sql)
        connection.commit()
        print(f"{mycursor.rowcount} tane kayıt güncellendi.")
    except mysql.connector.Error as err:
        print("Veritabanı işlemleri başarısız! Hata:", err)
        connection.rollback()
    finally:
        mycursor.close()
        connection.close()
        print("Veritabanı bağlantısı kapatıldı.".center(50))

update_product()
get_products()