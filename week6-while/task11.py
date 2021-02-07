enter_pass = input('enter password: ')
pass_ = 'qwerty123'
i = 1
if enter_pass == pass_:
    print('You entered to system :-)')
while enter_pass != pass_:
    print('incorrect password!!!')
    enter_pass = input('enter password: ')
    if enter_pass == pass_:
        print('You entered to system :-)')
        break
    i += 1
    if i == 5:
        print('You are blocked, because you entered incorrect password 5 times!!!')
        break
