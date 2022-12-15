t = int(input())
while t > 0:
    n = int(input())
    a = []
    while n > 0:
        a.append(int(input()))
        n -= 1
    a.sort()
    maxx = a.count(a[0])
    tmp = a[0]
    for i in range(1, len(a)):
        if a.count(a[i]) > maxx:
            maxx = a.count(a[i])
            tmp = a[i]
    print(tmp)
    t -= 1