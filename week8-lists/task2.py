from random import randint
lst = []

for i in range(10):
    lst.append(randint(1, 100))
# 1
# for i in lst:
#     print(i, end=' ')
# print()

# 2
# sum = 0
# for i in lst:
#     sum += i
# print(sum/len(lst))

# 3
# lst.sort()
# print("Min value in list: " + str(lst[0]))
# print("Max value in list: " + str(lst[-1]))

# 4
# lst.sort()
# print(lst[1])

# 5
for i in lst:
    if i % 2 == 0:
        print(i, end=' ')
print()
