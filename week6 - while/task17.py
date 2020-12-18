from random import randint
# heads and tails
player1Cash = 100
player2Cash = 100
# ht = randint(1, 2)
ht = 1
while player1Cash != 200 or player2Cash != 200:
    player1 = int(input('Player 1:\n1.Heads 2.Tails: '))
    player2 = int(input('Player 2:\n1.Heads 2.Tails: '))
    if player1 == ht:
        player1Cash += 9
    else:
        player1Cash -= 10
    if player2 == ht:
        player2Cash += 9
    else:
        player2Cash -= 10

if player2Cash > player1Cash:
    print('Player 2 win!!!')
else:
    print('Player 1 win!!!')
