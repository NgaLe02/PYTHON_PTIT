
n = int(input())

a = []

for i in range (n):
    a.append(list(int(x) for x in input().split()))
k = int(input())
up = 0
down = 0
for i in range (n - 1):
    for j in range (i + 1, n):
        up += a[i][j]
for i in range (1, n):
    for j in range (0, i):
        down += a[i][j]
if abs(up - down) <= k:
    print("YES")
else:
    print('NO')
print(abs(up - down))
