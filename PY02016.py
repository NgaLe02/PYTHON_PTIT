t = int(input())
while t > 0:
    n = int(input())
    l = [int(x) for x in input().split()]
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    maxx = 0
    res = 0
    # d : increasing
    for key, val in d.items():
        if val > maxx:
            maxx = val
            res = key

    if maxx > n // 2:
        print(res)
    else:
        print("NO")
    t -= 1