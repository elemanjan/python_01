n = int(input('enter a number: '))
count = 0
# for i in range(n, 0, -1):
#     if i % 2 == 0:
#         count += 1
#         n = i // 2
#         # print(i)
#     else:
#         count += 1\
# # print(count)
while n != 0:
    if n % 2 == 0:
        count += 1
        n = n // 2
    else:
        n = n - 1
        count += 1
print(count)
