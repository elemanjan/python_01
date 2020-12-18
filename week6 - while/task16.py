userWin = 0
compWin = 0
i = 0
while i < 5:
    user = int(input('Человек:\n1.Камень 2.Ножницы 3.Бумага: '))
    comp = int(input('Компьютер:\n1.Камень 2.Ножницы 3.Бумага: '))
    # if user == comp:
    #     print("ничья")
    if user == 1 and comp == 2:
        userWin += 1
    elif user == 1 and comp == 3:
        compWin += 1
    elif user == 2 and comp == 1:
        compWin += 1
    elif user == 2 and comp == 3:
        userWin += 1
    elif user == 3 and comp == 1:
        userWin += 1
    elif user == 3 and comp == 2:
        compWin += 1
    if userWin == 3 or compWin == 3:
        break
    i += 1
if userWin > compWin:
    print('User win!!!')
elif userWin == compWin:
    print('Draw')
elif userWin < compWin:
    print('Comp win!!!')
