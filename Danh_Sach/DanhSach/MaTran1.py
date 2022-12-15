
n = int(input())
a = []
for i in range(n):
    a.append(list(int(x) for x in input().split()))

k = int(input())


sumUp = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        sumUp += a[i][j]

sumDown = 0
for i in range(1, n):
    for j in range(i):
        sumDown += a[i][j]

x = abs(sumUp - sumDown)
if x > k:
    print('NO')
else:
    print('YES')
print(x)
