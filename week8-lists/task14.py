l = [1, 2, 3]
m = [11, 22, 33]
n = l + m
o = []

for i in range(1, len(n)):
    for j in range(len(n)):
        if n[j] % 10 == i:
            o.append(n[j])

print(o)
