from random import randint
n = []
for i in range(10):
    r = randint(0, 9)
    n.append(r)
l = n
print(l)
m = []
count = 0
for i in range(len(n)):
    for j in range(len(l)):
        if n[i] == l[j]:
            count += 1
        # else:
        #     count = 0
    if count == 1:
        m.append(n[i])
    count = 0
print(m)
