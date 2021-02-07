s = input('enter: ')
s = s.lower()
isVowels = True
if 'a' in s or 'e' in s or 'u' in s or 'o' in s or 'i' in s or 'y' in s:
    print(isVowels)
else:
    print(not isVowels)
