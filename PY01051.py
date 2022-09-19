def check(n):
    tong = 0
    for i in n:
        tong += int(i)
    tong = str(tong)
    tmp = tong[::-1]
    if(len(tong) > 1 and tmp == tong):
        return 1
    return 0

t = int(input())
while t > 0:
    n = input()
    if(check(n) == 1):
        print("YES")
    else:
        print("NO")
    t -= 1