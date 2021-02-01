filee = open('passStuds.txt', 'w')
scoreList = [line.strip().split() for line in open('grades.txt')]
count = 0
for score in scoreList:
    if int(score[1]) > 50 and int(score[2]) > 50 and int(score[3]) > 50:
        print(score[0], file=filee)
filee.close()
