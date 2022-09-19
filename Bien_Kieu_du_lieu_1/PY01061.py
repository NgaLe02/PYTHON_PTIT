import math
def snt(k):
    if k < 2: return 0
    for i in range (2, int(math.sqrt(k) + 1)):
        if k % i == 0:
            return 0
    return 1

def check(s):
    dau = 0
    cuoi = 0
    for i in range (0, 3):
        dau = dau * 10 + int(s[i])
    for i in range (-3, 0):
        cuoi = cuoi * 10 + int(s[i])
    if snt(dau) == 1 and snt(cuoi) == 1:
        return 1
    return 0

t = int(input())
while t > 0:
    s = input()
    if check(s) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1