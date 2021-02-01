filee = open('scores.txt', 'w')
scoreList = [line.strip().split() for line in open('class_scores.txt')]
for score in scoreList:
    if score[1].isdigit():
        print(score[0], int(score[1])+5, file=filee)
filee.close()
