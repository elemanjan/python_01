s = input('enter a word to encrypt: ')
fLen = 0
sLen = 0
thLen = 0
decryptStr = ""
keyLen = 0
if len(s) % 3 == 0:
    fLen = len(s) // 3
    sLen = (len(s) // 3) + fLen
    thLen = (len(s) // 3) + sLen
elif (len(s) % 3) == 2:
    fLen = (len(s) // 3) + 1
    sLen = ((len(s) // 3) + 1) + fLen
    thLen = len(s)-1
elif (len(s) % 3) == 1:
    fLen = (len(s) // 3) + 1
    sLen = (len(s) // 3) + fLen
    thLen = len(s)

fstStr = s[0:fLen]
sndStr = s[fLen:sLen]
thdStr = s[sLen:thLen+1]

for i in range(len(fstStr)):
    decryptStr += fstStr[i]
    decryptStr += sndStr[i]
    if i < len(thdStr):
        decryptStr += thdStr[i]
print(decryptStr)
