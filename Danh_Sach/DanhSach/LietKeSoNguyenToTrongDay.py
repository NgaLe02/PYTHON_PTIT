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

d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for key, value in d.items():
    if snt(key):
       print(f"{key} {value}")
