p = 0
for i in range(100000, 1000000):
    if str(i) == str(i)[::-1]:
        if i - p < 20:
            print(i, p)
        p = i