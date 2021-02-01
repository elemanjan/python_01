print('Enter a string values for list:')
l = []
for i in range(5):
    l.append(input())


for i in range(len(l)):
    l[i] = (l[i])[1:]
print(l)
