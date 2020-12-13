s = input('Enter a text: ')
vowels = 'aoiuye'
counter = 0
for i in range(len(s)):
    for j in vowels:
        if s[i] == j:
            counter += 1
print(counter)
