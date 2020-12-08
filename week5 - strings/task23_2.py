s = input('enter a word to encrypt: ')
fstStr = ""
sndStr = ""
thdStr = ""
decryptStr = ""
keyLen = 0
# c = len(s) % 3
if len(s) % 3 == 0:
    keyLen = len(s) // 3
elif (len(s) % 3) == 2:
    len(fstStr) = (len(s) // 3) + 1
    len(sndStr) = (len(s) // 3) + 1
elif (len(s) % 3) == 1:
    len(fstStr) = (len(s) // 3) + 1

print(len(fstStr))

# encryptStr = fstStr + sndStr + thdStr

# print(decryptStr)
