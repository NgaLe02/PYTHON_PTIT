
s = input()
while len(s) % 3 != 0:
    s = "0" + s
for i in range (0, len(s), 3):
    tmp = 0
    if s[i] == '1':
        tmp += 4
    if s[i + 1] == '1':
        tmp += 2
    if s[i + 2] == '1':
        tmp += 1
    print(tmp, end = '')
print()