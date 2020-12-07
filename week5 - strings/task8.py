s = input("text: ")
s = s.lower()
new_s = ""

for i in range(len(s)):
    if s[i].isalpha():
        new_s += s[i]
print(new_s)
