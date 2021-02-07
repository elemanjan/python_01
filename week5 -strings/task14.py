print("enter equal length words")
s1 = input('first word: ')
s2 = input('second word: ')

if len(s1) == len(s2):
    for i in range(len(s1)):
        print(s2[i]+s1[i], end='')
else:
    print('length of word does not equal!!!')
print()
