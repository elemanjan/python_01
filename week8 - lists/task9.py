from random import randint
l = []
for i in range(2, 13):
    l.append(i)
k = 0
n = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while k != 10001:
    n1 = randint(1, 6)
    n2 = randint(1, 6)
    sum = n1 + n2
    for i in range(len(l)):
        if sum == l[i]:
            n[i] += 1
    k += 1
m = {}
j = 2
for i in range(len(n)):
    m.update({j: (n[i] / 10000) * 100})
    j += 1
print(m)
summ = 0
for i in m:
    summ += m[i]

print(summ)
