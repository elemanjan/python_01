users = {'eleman': 'qwerty', 'deevve':'123456', 'bobby':'987654321', 'dad':'112233'}
user = input('enter user name: ')
pswd = input('enter user password: ')

isUser = 0
isPass = 0
for u in users:
    if user == u:
        isUser += 1
        if pswd == users[u]:
            isPass += 1
if isUser > 0:
    if isPass > 0:
        print('Welcome (:')
    else:
        print('Wrong password!')
else:
    print('Wrong login')

