import math

def snt(n):
    if n < 2: return 0
    for i in range (2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1

def uscln(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def tim_k(n):
    k = 1
    for i in range (2, n):
        if uscln(i, n) == 1:
            k = k + 1
    return k

t = int(input())
while t > 0:
    n = int(input())
    k = tim_k(n)
    #print(k)
    if snt(k) == 1:
        print("YES")
    else:
        print("NO")
    t = t - 1