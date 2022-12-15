
n = int(input())
a = []
for i in range(n):
    a.append(input())

ans = 0
for i in range(n):
    dem = a[i].count('C')
    ans += dem * (dem - 1) // 2

for i in range(n):
    dem = 0
    for j in range(n):
        if a[j][i] == 'C':
            dem += 1
    ans += dem * (dem - 1) // 2
print(ans)
