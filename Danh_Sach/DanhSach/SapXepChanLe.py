
n = int(input())
a = []
while True:
    for x in input().split():
        a.append(int(x))
    if len(a) == n:
        break

c = []
l = []
for i in a:
    if i % 2 == 0:
        c.append(i)
    else:
        l.append(i)

c.sort()
l = sorted(l, reverse=True)

chan = 0
le = 0
for i in a:
    if i % 2 == 0:
        print(c[chan], end = ' ')
        chan += 1
    else:
        print(l[le], end = ' ')
        le += 1