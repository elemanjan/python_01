""" 25.	Напишите программу, которая просит пользователя ввести число и распечатать, сколько чисел от 1 до N (включая N) делятся на 5 или 7, и список чисел.

Пример:
>>>
40
Есть 12 чисел, которые делятся на 5 и 7.
5,7,10,14,15,20,21,25,28,30,35,40, """

n = int(input('Enter number: '))
count = 0

for i in range(1, n+1):
    if i % 5 == 0 or i % 7 == 0:
        count += 1
        print(i, end=',')
print()
print("Есть", count, "чисел, которые делятся на 5 и 7.")
