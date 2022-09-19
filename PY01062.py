import math
def snt(k):
    if k < 2: return 0
    for i in range (2, int(math.sqrt(k) + 1)):
        if k % i == 0:
            return 0
    return 1

def check(s):
    scs = len(s)
    if snt(scs) == 0:
        return 0
    scsnt = 0
    for i in s:
        if snt(int(i)) == 1:
            scsnt += 1
    if scsnt > scs - scsnt:
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