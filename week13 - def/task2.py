def addSignToList(arr):
    for i in range(len(arr)):
        arr[i] += '!'
    return arr


arr = addSignToList(['salam', 'kandai', 'jakshyby'])
print(arr)

