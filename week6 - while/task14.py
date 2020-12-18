s = input('Введите 2 значение через запятую чтобы найти НОД : ')
s = s.split(',')
nod1 = int(s[0])
nod2 = int(s[1])
nod = 0

while nod1 != 0 and nod2 != 0:
    if nod1 > nod2:
        nod1 = nod1 % nod2
    else:
        nod2 = nod2 % nod1
print(nod1)
print(nod2)
print(nod1 + nod2)
