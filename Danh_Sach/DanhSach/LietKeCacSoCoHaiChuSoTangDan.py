
s = input()
a = []
l = len(s)
if l % 2 == 1:
    l -= 1
for i in range(0, l, 2):
    tmp = s[i:i+2]
    if not int(tmp) in a:
        a.append(int(tmp))
# a.sort()
print(*a)
