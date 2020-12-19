print('Please think of a number between 0 and 100!')
h = 100
num = 77
l = 0
while True:
    m = (h + l) // 2
    print('Is your secret number', m, '?')
    answer = input(
        "Enter 'h' to indicate the guess is too high.\nEnter 'l' to indicate the guess is too low.\nEnter 'c' to indicate I guessed correctly: ")
    if answer == 'h':
        h = m
    elif answer == 'l':
        l = m
    elif answer == 'c':
        print('Game over. Your secret number was:', m)
        break
