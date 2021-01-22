l = [61, 228, 9]
n = ''
s = []
for i in range(0, len(l)):
    s.append(str(l[i]))
t = 0
temp = 0
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if int(s[i][0]) > int(s[j][0]):
            temp += 1
    if temp == len(s)-1:
        n += s[i]
print(n)
