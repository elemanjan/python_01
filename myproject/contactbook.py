import sqlite3


class Users:

    def __init__(self, fName, lName, phone_number, email):
        self.fName = fName
        self.lName = lName
        self.phone_number = phone_number
        self.email = email

    def save(self):
        conn = sqlite3.connect('contacts.db')
        cur = conn.cursor()
        query = """INSERT INTO users (userid, fname, lname, number, email) VALUES(1, self.fName, self.lName, self.phone_number, self.email)"""
        cur.execute(query)
        conn.commit()
        conn.close()


print('Добро пожаловать в программу Контакты')
print('Введите свои контактные данные')

fName = input("Введите имя: ")
lName = input("Введите фамилию: ")
phone_number = input("Введите номер: ")
email = input("Введите почту: ")

user = Users(fName, lName, phone_number, email)
user.save()
