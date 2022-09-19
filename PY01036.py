t = int(input())
while t > 0:
    n = int(input())
    tong = float(0)
    if n % 2 == 1:
        for i in range(1, n + 1, 2):
            tong += float(1 / i)
    else:
        for i in range(2, n + 1, 2):
            tong += float(1 / i)
    print("{:.6f}".format(tong))
    t -= 1
