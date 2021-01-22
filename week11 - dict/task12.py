L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
userInp = 'a**a***'
userDict = {}
for i in range(len(userInp)):
    if userInp[i] != '*':
        userDict[i] = userInp[i]
res = []
for l in L:
    count = 0
    i = 0
    for k, v in userDict.items():
        if v == l[k]:
            count += 1
        i += 1
    if count == len(userDict.keys()):
        res.append(l)

print(res)
