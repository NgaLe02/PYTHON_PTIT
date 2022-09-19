import math

def stn(n):
    n = str(n)
    if len(n) < 2:
        return 0
    s = n[::-1]
    return n == s


n, m = [int(x) for x in input().split()]
array = []

for i in range (n):
    array.append(list(int(x) for x in input().split()))

mem = 0
for i in range (n):
    for j in range (m):
        if stn(array[i][j]) and array[i][j] > mem:
            mem = array[i][j]
if mem == 0:
    print("NOT FOUND")
else:
    print(int(mem))
    for i in range(n):
        for j in range(m):
            if array[i][j] == mem:
                print(f"Vi tri [{i}][{j}]")


# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 29 28 23
# 29 77 11 19
# 16 26 24 21
# 13 25 77 77
