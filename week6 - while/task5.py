n = int(input('enter a digit: '))
count = 0
i = 1
m = ""
while i <= n:
    if i % 5 == 0 or i % 7 == 0:
        count += 1
        m += str(i) + ','
    i += 1
print('Есть ' + str(count)+' чисел, которые делятся на 5 и 7.')
print(m)
