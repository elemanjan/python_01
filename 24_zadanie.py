""" 24.	Напишите программу используя циклы, чтобы получить следующий результат:
Вход: 8
Выход:
1
22
333
4444
55555
666666
7777777 """

n = int(input('Enter number: '))
t = 10
s = 1
lenn = 1

for i in range(1, n):
    for j in range(1, i+1):
        print(i, end='')

    print()
