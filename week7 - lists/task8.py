n = int(input('enter number: '))
i = 2
l = []
while n != 1:
    if n % i == 0:
        n = n // i
        l.append(i)
    else:
        i += 1

print(l)
