import math
def check1(s):
    tong = 0
    while(s > 0):
        tong += s % 10
        s = int(s / 10)
    return tong % 10 == 0

def check2(s):
    while(s > 10):
        a = s % 10
        s = int(s / 10)
        b = s % 10
        if(a - b != 2 and b - a != 2):
            return 0
    return 1

t = int(input())
while t > 0:
    s = int(input())
    if(check1(s) == 1 and check2(s) == 1):
        print("YES")
    else:
        print("NO")
    t -= 1