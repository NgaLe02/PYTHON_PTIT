import math

n = int(input())
a = [int(x) for x in input().split()]
a.sort()
for i in range(n - 1):
    for j in range(i + 1, n):
        if math.gcd(a[i], a[j]) == 1:
            print(f"{a[i]} {a[j]}")
