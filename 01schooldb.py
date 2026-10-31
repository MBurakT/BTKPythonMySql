import mysql.connector
import datetime as dt

host = "localhost"
user = "root"
password = "1234"
database = "schooldb"

values = [
    ("101", "Ahmet", "Yılmaz", dt.datetime(2005, 5, 17), "E"), 
    ("102", "Ali", "Can", dt.datetime(2005, 6, 17), "E"), 
    ("103", "Canan", "Tan", dt.datetime(2005, 7, 7), "K"), 
    ("104", "Ayşe", "Taner", dt.datetime(2005, 9, 23), "K"), 
    ("105", "Bahadır", "Toksöz", dt.datetime(2004, 7, 27), "E"), 
    ("106", "Ali", "Cenk", dt.datetime(2003, 8, 25), "E")
]

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
        print("Veritabanı bağlantısı başarısız! \nHata:", err)
        return # return None

def insert_students(values):
    connection = connect_database(
        host = host, 
        user = user, 
        password = password, 
        database = database
    )

    if connection is None:
        return # return None

    cursor = None
    try: 
        cursor = connection.cursor()
        sql = "INSERT INTO students (Number, Name, Surname, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
        
        cursor.executemany(sql, values)

        connection.commit()
        print(f"{cursor.rowcount} tane kayıt başarıyla eklendi.")

    except mysql.connector.Error as err:
        print("Veritabanı işlemi başarısız! \nHata:", err)
        connection.rollback() # Hata durumunda değişiklikleri geri al

    finally:
        if cursor: # not cursor is None
            cursor.close()

        if connection and connection.is_connected():
            connection.close()
            print("Veritabanı bağlantısı kapatıldı.")

insert_students(values = values)