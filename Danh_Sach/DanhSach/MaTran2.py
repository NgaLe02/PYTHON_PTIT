
n = int(input())
a = []
for i in range(n):
    a.append(list(int(x) for x in input().split()))

k = int(input())


sumUp = 0
for i in range(n):
    for j in range(n - i - 1):
        sumUp += a[i][j]

sumDown = 0
for i in range(n):
    for j in range(n - i, n):
        sumDown += a[i][j]

x = abs(sumUp - sumDown)
if x > k:
    print('NO')
else:
    print('YES')
print(x)
