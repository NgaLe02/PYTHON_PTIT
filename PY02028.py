import math

def snt(n):
    if n < 2:
        return 0
    for i in range (2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1


n = int(input())

l = [int(x) for x in input().split()]
a = []
prime = []
for i in l:
    if snt(i):
        a.append(1)
        prime.append(i)
    else:
        a.append(0)

prime.sort()
ind = 0
for i in range (len(l)):
    if a[i] == 0:
        print(l[i], end = ' ')
    else:
        print(prime[ind], end = ' ')
        ind += 1



