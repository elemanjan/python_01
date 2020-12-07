s = input('enter a word to decrypt: ')

even = ""
odd = ""
encryptStr = ""
decryptStr = ""
for i in range(len(s)):
    if i % 2 == 0:
        even += s[i]
    else:
        odd += s[i]

encryptStr = even + odd
even = ""
odd = ""

for i in range(len(encryptStr)):
    if i % 2 == 0:
        even += encryptStr[i]
    else:
        odd += encryptStr[i]
decryptStr = even + odd
print(decryptStr)
