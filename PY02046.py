import math


def snt(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1


n = int(input())

a = list(int(x) for x in input().split())

b = []
c = []
tong = 0
for i in a:
    if not(i in b):
        b.append(i)
        c.append(tong + i)
        tong += i
check = 0
# print(b)
# print(c)
for i in range(len(b)):
    if snt(c[i]):
        if snt(tong - c[i]):
            print(i)
            check = 1
            break
if check == 0:
    print("NOT FOUND")

