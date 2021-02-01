l = []

# 1

# for i in range(50):
#     l.append(i)
# print(l)

# 2

# for i in range(51):
#     l.append(i*i)
# print(l)

# 3
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_lst = []
new_lst.append(lst[0])
for i in range(1, len(lst)):
    new_lst.append(lst[i] * (i + 1))
print(new_lst)
print(len(new_lst[-1]))
