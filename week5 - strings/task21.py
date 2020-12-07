time = input('Введите время: ')
time = time.split(':')
print(time)
zone = int(input(
    'Выбери часового пояса:\n1.Восточный\n2.Центральный\n3.Горный\n4.Тихоокеанский\n'))
if zone == 1:
    zone = 11
elif zone == 2:
    zone = 12
elif zone == 3:
    zone = 13
elif zone == 4:
    zone = 14
time[0] = int(time[0])
if (time[0] - zone) < 0:
    temp = time[0] - zone
    time[0] = 24 - abs(temp)
    if 'pm' in time[1]:
        time[1] = time[1].replace('pm', 'am')
    elif 'am' in time[1]:
        time[1] = time[1].replace('am', 'pm')
else:
    time[0] = time[0] - zone
    print('else')

print(str(time[0])+":"+time[1])
