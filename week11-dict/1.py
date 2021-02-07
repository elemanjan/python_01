# def num(x):
#     for i in range(x):
#         print(i)
#         return
# num(10)


arr = [4,3,1,2]

arr[0], arr[arr[0]-1] = arr[arr[0]-1], arr[0]

print(arr)