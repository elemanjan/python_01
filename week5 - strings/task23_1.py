s = input('enter a word to encrypt: ')
fstStr = ""
sndStr = ""
thdStr = ""

for i in range(0, len(s), 3):
    fstStr += s[i]
for i in range(1, len(s), 3):
    sndStr += s[i]
for i in range(2, len(s), 3):
    thdStr += s[i]
encryptStr = fstStr + sndStr + thdStr
print(encryptStr)
