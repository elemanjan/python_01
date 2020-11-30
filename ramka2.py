h = int(input('height: '))
w = int(input('width: '))

for i in range(0, h):
    if i == 0 or i == h-1:
        for i in range(w):
            print('*', end='')
        print()
    else:
        print('*', end='')
        for i in range(0, w-2):
            print(end=' ')
        print('*')
