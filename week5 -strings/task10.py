s = ""
p = " "
l = int(input('How many addresses do you want enter: '))
for i in range(l):
    s += input('Enter email addresses: ') + p
if 'prof' in s:
    print("contains teacher emails")
else:
    print("only students emails")
