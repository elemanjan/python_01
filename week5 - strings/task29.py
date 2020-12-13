s = input('enter a word: ')
l = input('enter a letter: ')
ind = ""
for i in range(len(s)):
    if s[i] == l:
        ind += str(i) + " "
print('letter ' + l + ' indexes in ' + s + ': ' + ind)
