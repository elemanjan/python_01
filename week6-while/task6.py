n = int(input('enter a digit: '))
i = 0
sum = 0
while i <= n:
    sum += 2**i
    i += 1
print(sum)
