import math

def snt(k):
    if k < 2: return 0
    for i in range(2, int(math.sqrt(k) + 1)):
        if k % i == 0:
            return 0
    return 1

def check(s):
    for i in range (0, len(s)):
        if(s[i] == '2' or s[i] == '3' or s[i] == '5' or s[i] == '7'):
            if(snt(i) == 0):
                return 0
        else:
            if(snt(i) == 1):
                return 0
    return 1

t = int(input())
while t > 0:
    s = input()
    if(check(s) == 1):
        print("YES")
    else:
        print("NO")
    t -= 1