s = [20, 40, 60]

s[1] = 100
s.insert(1, 200)
s.pop(len(s)-1)
for i in s:
    print(i)
