cards = {'Валет': 11, 'Дама': 12, "Король": 13, "Туз": 14}
fstPoint = 0
sndPoint = 0
for i in range(3):
    card = input('1 игрок: Введите имя карты: ')
    for c in cards:
        if card.lower() == c.lower():
            fstPoint += cards[c]
for i in range(3):
    card = input('2 игрок: Введите имя карты: ')
    for c in cards:
        if card.lower() == c.lower():
            sndPoint += cards[c]

if fstPoint > sndPoint:
    print('1 игрок выиграл')
elif fstPoint < sndPoint:
    print('2 игрок выиграл')
elif fstPoint == sndPoint:
    print('Ничья')
     