s = input('enter message to decode: ')
evenStr = ""
oddStr = ""
encodedStr = ""
decodedStr = ""
for i in range(len(s)):
    if i % 2 == 0:
        evenStr += s[i]
    else:
        oddStr += s[i]
encodedStr = evenStr + oddStr
evenStr = ""
oddStr = ""
for i in range(len(encodedStr)):
    if i % 2 == 0:
        evenStr += encodedStr[i]
    else:
        oddStr += encodedStr[i]
decodedStr = evenStr + oddStr
print(decodedStr)
