import math

def snt(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def solve(x, n):
    s = str(x)
    if s[::-1] == s:
        return 0
    if int(s[::-1]) >= n:
        return 0
    if snt(x) and snt(int(s[::-1])):
        return x, int(s[::-1])
    return 0 
        
t = int(input())
while t > 0:
    n = int((input()))
    l = []
    for i in range(13, n):
        if(solve(i, n) != 0):
            a, b = solve(i, n)
            if not a in l and not b in l:
                l.append(a)
                l.append(b)
    print(*l)
    t -= 1