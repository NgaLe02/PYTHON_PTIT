def dao(n):
    m = 0
    while n > 0:
        m = m * 10 + n % 10
        n = int(n / 10)
    return m

t = int(input())
while t > 0:
    n = int(input())
    ok = 0
    m = 0
    tong = n
    for i in range (1, 1000):
        if tong % 7 == 0:
            ok = 1
            print(tong)
            break
        m = dao(n)
        tong = m + n
        n = tong
    if ok == 0:
        print("-1")
    t -= 1