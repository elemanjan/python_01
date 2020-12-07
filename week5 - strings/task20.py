s = input('Enter digits: ')
sLen = len(s)-1
digits = ""
digits2 = ""
count = 0
for i in range(sLen, -1, -1):
    digits += s[i]
    count += 1
    if count == 3:
        digits += " "
        count = 0
for i in range(len(digits)-1, -1, -1):
    digits2 += digits[i]
print(digits2)
