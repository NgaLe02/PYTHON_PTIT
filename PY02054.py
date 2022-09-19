n, m = ((int(x) for x in input().split()))

a = []

for i in range (n):
    b = list(int(x) for x in input().split())
    if n < m:
       for j in range (1, m - n + 1):
         b.pop(j)
    a.append(b)
if n > m:
   dif = n - m
   for i in range (dif):
       a.pop(i)
for i in a:
       print(*i)
