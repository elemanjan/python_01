from datetime import datetime

# filee = open('fullnames.txt', 'w')
wordList = [line.strip().split() for line in open('words.txt')]
# sName = [sName[i:i+1] for i in range(0, len(sName), 1)]
for i in range(len(wordList)):
    for j in range(len(wordList[i])):
        if 'ave' == wordList[i][j][1:4]:
            print(wordList[i][j])
# print(file=filee)
# filee.close()
