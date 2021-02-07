s = input('text: ')
isCorrect = False
if s[0] == "\"" and s[-1] == "\"":
    isCorrect = True
else:
    isCorrect = False

print(isCorrect)
