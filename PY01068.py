from itertools import combinations

n, k = map(int, input().split())

a = list(set(str(x) for x in input().split()))
a.sort()
s = combinations(a, k)

for i in s:
    print(*i)