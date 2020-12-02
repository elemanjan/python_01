n = int(input('Enter number: '))
s = 10000
temp = 0
for i in range(5):
    temp = n // s
    print(temp % 10)
    s = s // 10
