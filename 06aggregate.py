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

    sql = "SELECT name, price FROM products"
    sql = "SELECT COUNT(*) FROM products"
    sql = "SELECT COUNT(*) FROM products WHERE price > 2000"
    sql = "SELECT AVG(price) FROM products"
    sql = "SELECT SUM(price) FROM products"
    sql = "SELECT MAX(price) FROM products"
    sql = "SELECT MIN(price) FROM products"
    sql = "SELECT name FROM products WHERE price = (SELECT MAX(price) FROM products)"
    sql = "SELECT name FROM products"

    mycursor.execute(sql)
    datas = mycursor.fetchall()

    for data in datas:
        print(data)

    mycursor.close()
    connection.close()
    print("Veritabanı bağlantısı kapatıldı.".center(50))

get_products()