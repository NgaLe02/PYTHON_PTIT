import math

def check(n):
    tong = 0
    for i in n:
        tong += math.factorial(int(i))
    if tong == int(n):
        return 'Yes'
    return 'No'

t = int(input())
while t > 0:
    n = input()
    print(check(n))
    t -= 1