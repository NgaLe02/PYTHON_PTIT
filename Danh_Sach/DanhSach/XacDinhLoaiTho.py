
n = int(input())
a = []
for i in range(n):
    a.append(input().split())

ans = []
doDai  = 0
i = 0
while i < n: 
    doDai = len(a[i])
    if doDai == 7:
        ans.append(2)
        i = i + 4
    elif doDai == 6:
        i += 2
        if i + 1 >= n or len(a[i + 1]) == 7:
            ans.append(1)

print(len(ans))
print(*ans, sep= '\n')