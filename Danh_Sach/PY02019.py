import math


n = int(input())
list = [int(x) for x in input().split()]
list.sort()
for i in range (n - 1):
     for j in range (i + 1, n):
         if math.gcd(list[i], list[j]) == 1:
             print(f"{list[i]} {list[j]}")

