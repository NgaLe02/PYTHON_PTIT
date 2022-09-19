import math
def snt(k):
    if k < 2: return 0
    for i in range (2, int(math.sqrt(k) + 1)):
        if k % i == 0:
            return 0
    return 1

def check(n):
    tong = 0
    for i in n:
        tong += int(i)
    if snt(tong) == 1:
        return 1
    return 0

t = int(input())
while t > 0:
    n = input()
    if check(n) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1