s = input('enter text: ')
s = s.strip()
s2 = ""
c = 0
for i in range(len(s)-1, -1, -1):
    s2 += s[i]

for i in range(len(s2)):
    if s2[i] == s[i]:
        c += 1
if c == len(s2):
    print("Text is Polyndrom")
else:
    print("Text is not Polyndrom")
