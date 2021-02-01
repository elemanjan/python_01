l = []
for i in range(10):
    l.append(i)
print(l)
temp = []
for i in range(1, len(l)-1):
    temp.append(i)
temp.insert(0, l[-1])
temp.append(l[0])
print(temp)
