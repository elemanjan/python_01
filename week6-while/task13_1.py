text = input('enter a text: ')
letter = input('enter a letter: ')
index = 0
contains = False
while index < len(text):
    if text[index] == letter:
        print(index)
        contains = True
        break
    index += 1
if not contains:
    print('letter not found')
