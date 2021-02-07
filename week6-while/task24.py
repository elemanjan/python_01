n = int(input('How many integer numbers do you enter?: '))
summ = 0
count = 1
while n >= count:
    print('enter', count, 'number: ', end='')
    a = int(input())
    count += 1
    summ += a
    if a == 0:
        break
print('Summ:', summ)
print('Avarage:', summ/(count-1))
