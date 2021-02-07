import re

userPass = input('Enter password: ')

if re.fullmatch(r'[A-Za-z0-9$#@]{8,}', userPass):
    print('Valid password')
else:
    print('Password is not valid!!!')
