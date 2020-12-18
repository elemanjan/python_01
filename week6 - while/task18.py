country = 'Columbia'
country = country.lower()
new_ctr = ""
for i in range(len(country)):
    new_ctr += "-"
error = 0
count = 0
ind = 0
while error < 5:
    l = input('Guess the country by letter: ')
    count = 0
    for i in range(len(country)):
        if l == country[i]:
            new_ctr = new_ctr[:i] + l + new_ctr[i+1:]
            print(new_ctr)
            count = 1
    if count == 0:
        print('letter does not exist!!!')
        error += 1
