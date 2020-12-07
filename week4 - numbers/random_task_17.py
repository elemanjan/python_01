""" Напишите программу игры на умножение для детей. Программа должна дать игроку десять случайно сгенерированных вопросов на умножение. После каждого из них программа должна сказать им, правильно ли они поняли или нет, и каков правильный ответ.
Вопрос 1: 3 x 4 = 12
Верно!
Вопрос 2: 8 x 6 = 44
Неправильно. Ответ 48.
Вопрос 10: 7 x 7 = 49
Верно.
"""
from math import *
count = 0
for i in range(1600, 2020):
    if i % 4 == 0 and i % 100 != 0:
        count += 1
print(count)
