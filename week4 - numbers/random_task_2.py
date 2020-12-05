from random import randint
n = randint(1, 10)

m = int(input('Угадайте число: '))
if n == m:
    print('Вы угадали :)')
else:
    print('Вы не угадали :(')
