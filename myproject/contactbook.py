import sqlite3


class Users:

    def __init__(self, fName, lName, phone_number, email):
        self.fName = fName
        self.lName = lName
        self.phone_number = phone_number
        self.email = email

    def saveUser(self):
        conn = sqlite3.connect('contacts.db')
        cur = conn.cursor()
        param = (self.fName, self.lName, self.phone_number, self.email)
        query = """INSERT INTO users(fname,lname,phone_number,email)
        VALUES(?, ?, ?, ?)"""
        # uid = cur.execute("SELECT userid from")
        # cur.execute(, param)
        try:
            conn.execute(query, param)
            print("Контакт успешно сохранен!")
        except sqlite3.IntegrityError as e:
            print("Error occurred: ", e)
        conn.commit()
        conn.close()

    def printUsers(self):
        conn = sqlite3.connect('contacts.db')
        cur = conn.cursor()
        sql_query = "SELECT * FROM users"
        cur.execute(sql_query)
        while True:
            next_row = cur.fetchone()
            if next_row:
                print(next_row)
            else:
                break

    def addPeople(self):
        conn = sqlite3.connect('contacts.db')
        cur = conn.cursor()

        fnameList = [line.strip().split() for line in open('fullnames.txt')]
        param = []
        param_t = ()
        for i in range(len(fnameList)):
            for j in range(len(fnameList[i])):
                param.append(fnameList[i][j])
            eml = fnameList[i][0]+fnameList[i][1]+'@'+'gmail.com'
            param.append(eml)
            param_t = tuple(param)
            cur.executemany("""INSERT INTO users(fname,lname,phone_number,email)
            VALUES(?, ?, ?, ?)""", (param_t,))
            conn.commit()
            param.clear()
            param_t = tuple(param)
        conn.close()

    def searchPeople(self):
        name = input("Введите имя для поиска: ")
        conn = sqlite3.connect('contacts.db')
        cur = conn.cursor()
        sql_query = "SELECT * FROM users"
        cur.execute(sql_query)
        conn.commit()
        usersList = cur.fetchall()
        # print(usersList)
        foundUsers = []
        for i in usersList:
            for j in i:
                if name == [j][0]:
                    # print()
                    foundUsers.append(i)
        if len(foundUsers) > 0:
            print("Найденные контакты:", end='\n')
            for fuser in foundUsers:
                print(fuser)
        else:
            print("Не найден контакт с именем " + name + "!")


print('Добро пожаловать в программу Контакты')
print('Введите свои контактные данные')

# fName = input("Введите имя: ")
# lName = input("Введите фамилию: ")
# phone_number = input("Введите номер: ")
# email = input("Введите почту: ")


# user = Users(fName, lName, phone_number, email)
# user.saveUser()
user = Users('sdcsd', 'ecsdc', 897239123, '21dsds')
# user.addPeople()
# user.printUsers()
user.searchPeople()
