from random import randint
# n = [1, 0, 1, 0, 0, 1, 0, 0, 0, 0]
n = []
for i in range(20):
    r = randint(0, 1)
    n.append(r)
max1 = 0
max2 = 0
for i in range(len(n)):
    if n[i] == 0:
        max1 += 1
    else:
        if max1 >= max2:
            max2 = max1
            max1 = 0
if max1 >= max2:
    max2 = max1
print(n)
print(max2)
