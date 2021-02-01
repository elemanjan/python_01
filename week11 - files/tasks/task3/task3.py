from datetime import datetime

filee = open('passStuds.txt', 'w')
userList = [line.strip().split(',') for line in open('logfile.txt')]

FMT = '%H:%M'


for score in userList:
    t = datetime.strptime(score[2].strip(), FMT) - \
        datetime.strptime(score[1].strip(), FMT)
    if t.seconds//60 > 60:
        print(score[0], file=filee)
filee.close()
