n = int(input('Enter number: '))
c = 0
prime = True
for i in range(2, n):
    if n % i == 0:
        prime = False
        break
if prime:
    print("Простое число")
else:
    print("Не простое число")
