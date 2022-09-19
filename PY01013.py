
import math
def snt(n):
    if n < 2: return 0
    for i in range (2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1

def tcs(n):
    tong = 0
    while n > 0:
        tong += n % 10
        n = int(n / 10)
    return tong

def usc(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

t = int(input())
while t > 0:
    a, b = [int(x) for x in input().split()]
    if(snt(tcs((usc(a, b)))) == 1):
        print("YES")
    else:
        print("NO")
    t -= 1