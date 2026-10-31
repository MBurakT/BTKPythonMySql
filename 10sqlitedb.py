import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM customers")

datas = cursor.fetchall()

for data in datas:
    print(data[1])

connection.close()