x = input('enter: ')
xs = ""
for i in range(len(x)):
    if x[i].isdigit():
        xs += x[i]
    elif x[i] == '(':
        xs += '*'
        xs += x[i]
    elif x[i].isalpha():
        if x[i-1].isdigit():
            xs += '*'
            xs += x[i]
        elif x[i-1] == '(':
            xs += x[i]
    else:
        xs += x[i]
print(xs)
