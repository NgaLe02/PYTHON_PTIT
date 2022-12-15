def cmp(s):
    return len(s)

f = open("VANBAN.in", "r")
lines = f.readlines()

d = {}
a = []
for i in lines:
    for j in i.strip().split():
        if j == j[::-1]:
            a.append(j)
            if j in d:
                d[j] += 1
            else:
                d[j] = 1

a = sorted(a, key = cmp, reverse=True)
maxx = len(a[0])

for key, val in d.items():
    if len(key) == maxx:
        print(f"{key} {val}")

