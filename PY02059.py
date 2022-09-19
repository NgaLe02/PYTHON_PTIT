import math

def snt(n):
    if n < 2:
        return 0
    for i in range (2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1


n, m = [int(x) for x in input().split()]
array = []

for i in range (n):
    array.append(list(int(x) for x in input().split()))

mem = 0
for i in range (n):
    for j in range (m):
        if snt(array[i][j]) and array[i][j] > mem:
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
# 23 21 26 10
# 13 13 22 14
# 28 29 28 23
# 29 19 11 19
# 16 26 24 21
# 13 25 21 29
