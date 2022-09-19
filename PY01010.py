t = int(input())
while t > 0:
    a = input()
    dau = int(a[:2])
    cuoi = int(a[-2:])
    if dau == cuoi:
        print("YES")
    else:
        print("NO")
    t -= 1