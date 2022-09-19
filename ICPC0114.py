import math

def snt(n):
    if n < 2:
        return 0
    for i in range (2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1

def check(n):
    if snt(int(n)) == 0:
        return 0
    daoN = n[::-1]
    if snt(int(daoN)) == 0:
        return 0
    tong = 0
    for i in n:
        if snt(int(i)) == 0:
            return 0
        tong += int(i)
    if snt(tong) == 0:
        return 0
    return 1
t = int(input())
while t > 0:
    n = input()
    if check(n) == 1:
        print('Yes')
    else:
        print('No')
    t -= 1