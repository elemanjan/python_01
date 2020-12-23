l = []
l.append(1)
for i in range(1, 12):
    l.append('1')
nol = '0'
for i in range(2, len(l)+len(l)-2, 2):
    l.insert(i, nol)
    nol += '0'
print(l)
