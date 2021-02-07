s = input('enter: ')
if len(s) < 3:
    print(s)
else:
    if s[-3:] == 'ing':
        s = s + 'ly'
        print(s)
    else:
        s = s + 'ing'
        print(s)
