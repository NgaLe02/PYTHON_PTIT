while True:
    a = [int(x) for x in input().split()]
    if a[0] == a[1] == a[2] == a[3] == 0:
        break
    dem = 0
    while True:
        if a[0] == a[1] == a[2] == a[3]:
            break
        mem = a[0]
        for i in range(3):
            a[i] = abs(a[i] - a[i + 1])
        a[3] = abs(a[3] - mem)
        dem += 1
    print(dem)