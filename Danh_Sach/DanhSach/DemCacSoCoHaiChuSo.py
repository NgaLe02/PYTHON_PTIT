
s = input()
l = len(s)
if l % 2 == 1:
    l -= 1
d = {}
for i in range(0, l, 2):
    tmp = s[i:i+2]
    if int(tmp) in d:
        d[int(tmp)] += 1
    else:
        d[int(tmp)] = 1

for key, val in d.items():
    print(f"{key} {val}")
