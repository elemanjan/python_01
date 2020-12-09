s = input('enter a word to encrypt: ')
fstStr = s[0:fLen]
sndStr = 0
thdStr = 0
decryptStr = ""
keyLen = 0
if len(s) % 3 == 0:
    fLen = len(s) // 3
    snLen = len(s) // 3
    thLen = len(s) // 3
elif (len(s) % 3) == 2:
    fLen = (len(s) // 3) + 1
    snLen = (len(s) // 3) + 1
elif (len(s) % 3) == 1:
    fLen = (len(s) // 3) + 1
