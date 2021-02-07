s = input("enter a word: ")
l = input("enter a letter: ")
count = 0
for i in range(len(s)):
    if l == s[i]:
        count += 1
print(count)
