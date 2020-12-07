s = input('enter message to encode: ')
evenStr = ""
oddStr = ""
for i in range(len(s)):
    if i % 2 == 0:
        evenStr += s[i]
    else:
        oddStr += s[i]
encodedStr = evenStr + oddStr
print(encodedStr)
