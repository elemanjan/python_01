s = input("enter a word: ")
l = input("enter a letter: ")
count = 0
for i in range(len(s)):
    if l == s[i]:
        count += 1
if count > 0:
    print(s+" contains " + l)
else:
    print(s+" does not contains " + l)
