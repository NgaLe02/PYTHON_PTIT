import math

def snt(k):
    if k < 2: return 0
    for i in range(2, int(math.sqrt(k) + 1)):
        if k % i == 0:
            return 0
    return 1

def check(s):
    tong = 0
    for i in range (0, len(s)):
        tong += int(s[i])
        if(i % 2 == 0):
            if(int(s[i]) % 2 == 1):
                return 0
        else:
            if(int(s[i]) % 2 == 0):
                return 0
    if snt(tong) == 0:
        return 0
    return 1

t = int(input())
while t > 0:
    s = input()
    if check(s) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1