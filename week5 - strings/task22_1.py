s = input('enter a word to encrypt: ')

even = ""
odd = ""
encryptStr = ""

for i in range(len(s)):
    if i % 2 == 0:
        even += s[i]
    else:
        odd += s[i]

encryptStr = even + odd
print(encryptStr)
