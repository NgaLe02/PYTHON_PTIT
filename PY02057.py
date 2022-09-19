
n, m = [int(x) for x in input().split()]
array = []

for i in range (n):
    array.append(list(int(x) for x in input().split()))

minn = 10001
maxx = -1
for i in range (n):
    for j in range (m):
        if array[i][j] < minn:
            minn = array[i][j]
        if array[i][j] > maxx:
            maxx = array[i][j]
ok = 0
ans = maxx - minn
for i in range(n):
    for j in range(m):
        if array[i][j] == ans:
            if ok == 0:
                print(ans)
                print(f"Vi tri [{i}][{j}]")
                ok = 1
            else:
                print(f"Vi tri [{i}][{j}]")
if ok == 0:
    print("NOT FOUND")



# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 67 28 23
# 29 77 11 67
# 16 51 24 21
# 13 25 77 77
