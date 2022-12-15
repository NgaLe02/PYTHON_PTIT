import math

def snt(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def stn(n):
    s = str(n)
    if len(s) < 2:
        return 0
    if s != s[::-1]:
        return 0
    return 1

n, m = map(int, input().split())
a = []

for i in range(n):
    a.append(list(int(x) for x in input().split()))

maxx = -1
for i in a:
    for j in i:
        if stn(j) and j > maxx:
            maxx = j
if maxx == -1:
    print('NOT FOUND')
else:
    print(maxx)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxx:
                print(f"Vi tri [{i}][{j}]")

