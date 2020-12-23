L = []
M = []
N = []
for i in range(5):
    L.append(int(input('enter values for L: ')))
print()
for i in range(5):
    M.append(int(input('enter values for M: ')))
for i in range(len(L)):
    N.append(L[i]+M[i])

print(L)
print(M)
print('N:', N)
