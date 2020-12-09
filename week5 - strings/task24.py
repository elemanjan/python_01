x = input('enter: ')
preX = ""
aPower = x[-1:]
s = ""
for i in range(len(x)):
    if x[i].isdigit():
        preX += x[i]
    if x[i] == 'x':
        s += x[i]
        break
x = int(preX) * int(aPower)
aPower = int(aPower)
if aPower != 2:
    print(str(x)+s+"^"+str(aPower-1))
else:
    print(str(x)+s)
