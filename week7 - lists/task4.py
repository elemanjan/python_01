lst = eval(input('enter number from 1 to 12: '))

for i in range(len(lst)):
    if lst[i] > 10:
        lst[i] = 10
print(lst)
