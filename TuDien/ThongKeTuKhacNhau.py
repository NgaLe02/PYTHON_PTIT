import re
n = int(input())
a = []
for i in range(n):
    s = input().lower()
    x = re.findall("[\w\s]+", s)
    for i in x:
        for j in i.split():
            a.append(j)
        
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
for i in d:
    print(i[0], i[1])
