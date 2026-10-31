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
    sql = "SELECT * FROM products WHERE name LIKE '%Samsung%'"

    mycursor.execute(sql)
    datas = mycursor.fetchall()
    # data = mycursor.fetchone()

    for data in datas:
        print(data)

    mycursor.close()
    connection.close()
    print("Veritabanı bağlantısı kapatıldı.".center(50))

def get_products_byid(id):
    connection = connect_database(
        host = "localhost", 
        user = "root", 
        password = "1234", 
        database = "node-app"
    )
    if not connection:
        return

    mycursor = connection.cursor()
    sql = "SELECT * FROM products WHERE id = %s"

    mycursor.execute(sql, (id,))
    data = mycursor.fetchone()
    print(data)

    mycursor.close()
    connection.close()
    print("Veritabanı bağlantısı kapatıldı.".center(50))

get_products()
get_products_byid(3)