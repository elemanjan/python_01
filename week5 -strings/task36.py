s = input('enter a sequence: ')
w = input('enter a word: ')
count = 0
i = len(w)
j = 0
while i < len(s):
    s2 = s[j:i]
    if s2 == w:
        count += 1
        i += len(w)
        j += len(w)
    else:
        count = 0
        j = j + 1
        i = i + 1

print(count)
