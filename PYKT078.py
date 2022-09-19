t = int(input())
while t > 0:
    n, m = [int(x) for x in input().split()]
    a = list(int(x) for x in input().split())
    maxx = a[0]
    ind = 0
    for i in range (0, n):
        if a[i] > maxx:
            maxx = a[i]
            ind = i
    a.insert(ind, m)
    b = []
    i = 0
    while i <= n:
        if a[i] < 0:
            b.append(a[i])
            a.pop(i)
            n = n - 1
        else:
            i = i + 1
    b.extend(a)
    print(*b)
    t = t - 1