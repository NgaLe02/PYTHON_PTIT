
s = input()
k = int(input())

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
dd = sorted(d.keys())
check = 0
for key in dd:
    if d[key] >= k:
       print(f"{key} {d[key]}")
       check = 1

if check == 0:
    print('NOT FOUND')
