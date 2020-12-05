x = int(input('Введите число: '))
y = int(input('Введите степень: '))

s = x**y
print(s)
lastNum = s % 10
s = lastNum ** y
print(s)
