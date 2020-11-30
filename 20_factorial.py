n = int(input('Enter factorial: '))
sum = 1
if n == 1 or n == 0:
    sum = 1
else:
    for i in range(1, n+1):
        sum *= i
print(sum)
