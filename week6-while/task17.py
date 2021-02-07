from random import randint
# heads and tails
player1Cash = 100
player2Cash = 100
# ht = randint(1, 2)
ht = 1
while player1Cash <= 200 and player2Cash > 0:
    player1 = int(input('Player 1:\n1.Heads 2.Tails: '))
    player2 = int(input('Player 2:\n1.Heads 2.Tails: '))
    if player1 == ht:
        player1Cash += 9
        # print('player1: ', player1Cash)
    else:
        player1Cash -= 10
        print(player1Cash)
    if player2 == ht:
        player2Cash += 9
        print(player2Cash)
    else:
        player2Cash -= 10
        # print('player2: ', player2Cash)

if player2Cash > player1Cash:
    print('Player 2 win!!!')
else:
    print('Player 1 win!!!')
