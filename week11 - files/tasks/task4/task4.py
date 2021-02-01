from datetime import datetime

filee = open('students2.txt', 'w')
studList = [line.strip().split() for line in open('students.txt')]

for students in studList:
    s1, s2 = students[0].capitalize(), students[1].capitalize()
    s4 = '(301)' + students[3]
    print(s1, s2, students[2], s4, file=filee)
filee.close()
