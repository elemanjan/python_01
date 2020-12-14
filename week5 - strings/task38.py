s = input('enter a sequence: ')
w = "bob"
count = 0
i = len(w)
j = 0
while i < len(s):
    s2 = s[j:i]
    if s2 == w:
        count += 1
    i += 1
    j += 1
print(count)
