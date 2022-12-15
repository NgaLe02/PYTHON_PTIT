
import math

def snt(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def check(n):
    if snt(n) == 0:
        return 0
    if snt(int(str(n)[::-1])) == 0:
        return 0
    tcs = 0
    for i in str(n):
        if snt(int(i)) == 0:
            return 0
        tcs += int(i)
    if snt(tcs) == 0:
        return 0 
    return 1

t = int(input())
while t > 0:
    n = int(input())
    if check(n):
        print('Yes')
    else:
        print('No')
    t -= 1