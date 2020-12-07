""" s = input('text: ')
new_s = s
new_s = new_s.replace(s[1], '*', 1)
s3 = "!!!"
sLen = len(s)
new_s = new_s + s3
print(new_s)

 """
s = input('text: ')
new_s = ""
s3 = "!!!"
for i in range(len(s)):
    if i == 1:
        new_s += '*'
    else:
        new_s += s[i]
print(new_s+s3)
