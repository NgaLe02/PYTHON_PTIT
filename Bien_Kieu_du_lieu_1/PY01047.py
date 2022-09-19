import math
def snt(k):
    if k < 2: return 0
    for i in range (2, int(math.sqrt(k) + 1)):
        if k % i == 0:
            return 0
    return 1

def solve(s):
    s = s[-4:]
    n = 0
    for i in s:
        n = n * 10 + int(i)
    if(snt(n) == 1):
        print("YES")
    else:
        print("NO")

t = int(input())
while t > 0:
    s = input()
    solve(s)
    t -= 1