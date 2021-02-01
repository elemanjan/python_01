l = [61, 228, 9, 115]
l.sort()
# l.reverse()
s = l
lst = []
for i in range(0, len(l)-1):
    if str(l[i])[0] < str(l[i+1])[0]:
        l[i], l[i+1] = l[i+1], l[i]

tsl = []
# for i in s:
#     for j in i:
#         tsl.append(j)
#     lst.append(tsl)
# # print(i)
print(l)
