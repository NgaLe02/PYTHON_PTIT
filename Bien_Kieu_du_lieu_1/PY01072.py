
from itertools import combinations

n, k = [int(x) for x in input().split()]
l = list(set(int(x) for x in input().split()))

l.sort()

s = combinations(l, k)
for i in s:
    print(*i)

