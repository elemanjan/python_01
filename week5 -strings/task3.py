"""
Напишите программу, которая просит пользователя ввести строку. Затем программа должна напечатать следующее:
    общее количество символов в строке
    строка повторяется 10 раз
    первый символ строки (помните, что индексы строк начинаются с 0)
    первые три символа строки
    последние три символа строки
    строку задом наперед
    седьмой символ строки, если строка достаточно длинная, и сообщение в противном случае
    строка с удаленными первым и последним символами
    строка во всех заглавных буквах
    строка, в которой каждое а заменено на е
    строку каждая буква заменяется на пробел

"""
s = input('Enter text: ')
# 1
sLen = len(s)
print(len(s))

# 2
for i in range(10):
    print(s)

# 3
print(s[0])

# 4
print(s[0:3])

# 5
print(s[-3:])

# 6
sLen = sLen - 1
for i in range(sLen, -1, -1):
    print(s[i])

# 7
if sLen >= 7:
    print(s[6])
else:
    print('7 symbol does not exist')

# 8
print(s[1:-1])

# 9
print(s.upper())

# 10
print(s.replace('a', 'e'))

# 11
print(s.replace(s, " "))