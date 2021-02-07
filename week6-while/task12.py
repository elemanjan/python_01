enter = int(input('enter your test result : '))
n = 0
countA = 0
avg = 0.0
count = 0
while enter > 0:
    if enter >= 80:
        countA += 1
    enter = int(input('enter your test result : '))
    count += 1
    n += enter
avg = n / count
print('Results with A: ' + str(countA))
print('Avarage point: ' + str(avg))
