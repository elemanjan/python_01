s = input("enter a word: ")
l = input("enter a letter: ")
ind = 0
count = 0
for i in range(len(s)):
    if l == s[i]:
        count += 1
        ind = i
        break
if count > 0:
    print(s+" contains " + l + " in index ", ind)
else:
    print(s+" does not contains " + l)
