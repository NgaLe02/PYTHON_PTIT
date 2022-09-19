import math
def snt(k):
    if k < 2: return 0
    for i in range (2, int(math.sqrt(k) + 1)):
        if k % i == 0:
            return 0
    return 1

def check(n):
    ssnt = 0
    scs = len(n)
    for i in n:
        a = int(i)
        if snt(a) == 1:
            ssnt += 1
    if snt(scs) == 1 and ssnt > scs - ssnt:
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