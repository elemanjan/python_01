lst = [8, 9, 10]
# 1
lst[1] = 17

# 2
for i in range(4, 7):
    lst.append(i)
print(lst)

# 3
lst.pop(0)
print(lst)

# 4
lst.sort()

# 5
new_lst = lst + lst
new_lst[3] = 25
print(new_lst)

# 6
