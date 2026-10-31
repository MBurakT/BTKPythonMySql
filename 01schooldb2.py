import mysql.connector
import datetime as dt

class Student:
    connection = mysql.connector.connect(
        host = "localhost", 
        user = "root", 
        password = "1234",
        database = "schooldb"
    )
    mycursor = connection.cursor()

    def __init__(self, number, name, surname, birthdate, gender):
        self.number = number
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def save_student(self):
        sql = "INSERT INTO students (Number, Name, Surname, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
        value = (self.number, self.name, self.surname, self.birthdate, self.gender)
        
        Student.mycursor.execute(sql, value)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")

        except mysql.connector.Error as err:
            print("Hata:", err)

        finally:
            Student.connection.close()

    @staticmethod
    def save_students(students):
        sql = "INSERT INTO students (Number, Name, Surname, Birthdate, Gender) VALUES (%s, %s, %s, %s, %s)"
        values = students
                
        Student.mycursor.executemany(sql, values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt eklendi.")
        
        except mysql.connector.Error as err:
            print("Hata:", err)
        
        finally:
            Student.connection.close()

# ahmet = Student("202", "ahmet", "yılmaz", dt.datetime(2005, 5, 17), 'E')
# ahmet.save_student()

values = [
    ("301", "Ahmet", "Yılmaz", dt.datetime(2005, 5, 17), "E"), 
    ("302", "Ali", "Can", dt.datetime(2005, 6, 17), "E"), 
    ("303", "Canan", "Tan", dt.datetime(2005, 7, 7), "K"), 
    ("304", "Ayşe", "Taner", dt.datetime(2005, 9, 23), "K"), 
    ("305", "Bahadır", "Toksöz", dt.datetime(2004, 7, 27), "E"), 
    ("306", "Ali", "Cenk", dt.datetime(2003, 8, 25), "E")
]

Student.save_students(values)