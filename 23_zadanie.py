n = int(input('Enter number: '))
s = 10000
for i in range(5):
    n = n // s
    print(n)
    s = s // 10
