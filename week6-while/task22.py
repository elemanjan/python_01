from random import randint

rNum = randint(1, 20)
error = 0
name = input('Здравствуйте, как Вас зовут? ')
print('Что ж, ' + name + ' я думаю о числе от 1 до 20.')
n = int(input('Сделать предположение: '))
while error < 6:
    if n > rNum:
        print('Ваше предположение завышено!')
        n = int(input('Сделать предположение: '))
        error += 1
    elif n < rNum:
        print('Ваше предположение занижено!')
        n = int(input('Сделать предположение: '))
        error += 1
    elif n == rNum:
        print('Хорошая работа, ' + name +
              '! Вы угадали мой номер за ' + str(error) + ' попытки!')
        break
