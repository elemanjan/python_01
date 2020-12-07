s = input('Enter a word: ')
s1 = ""
s2 = ""
for i in range(len(s)):
    if s[i] == 'a':
        s2 += s[i:]
        break
    else:
        s1 += s[i]
print(s1)
print(s2)
