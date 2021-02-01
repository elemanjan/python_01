from datetime import datetime

# filee = open('fullnames.txt', 'w')
fnameList = [line.strip().split() for line in open('fullnames.txt')]
sName = input('Enter to search full names by initials:')
sName = [sName[i:i+1] for i in range(0, len(sName), 1)]
# print(len(fnameList))
count = 0
for i in range(len(fnameList)):
    if len(sName) == len(fnameList[i]):
        count = 0
        for j in range(len(sName)):
            if sName[j] == fnameList[i][j][0:1]:
                count += 1
        if count == len(sName):
            print(fnameList[i])
# print(file=filee)
# filee.close()
