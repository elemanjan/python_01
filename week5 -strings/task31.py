fName = input('enter your f name: ')
sName = input('enter your s name: ')
lenn = len(fName)+len(sName)
skl = fName + " " + sName
pass_ = ""
for i in range(lenn):
    if i < len(fName):
        pass_ += fName[i]
    if i < len(sName):
        pass_ += sName[i]
print('Your credentials are: ' + skl)
print('Your password is : ' + pass_)
