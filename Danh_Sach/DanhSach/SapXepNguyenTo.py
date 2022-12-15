import math
def snt(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

n = int(input())
a = [int(x) for x in input().split()]
b = []
for i in a:
    if snt(i):
        b.append(i)

b.sort()
ind = 0
for i in a:
    if snt(i):
        print(b[ind], end = ' ') 
        ind += 1
    else:
        print(i, end = ' ')

