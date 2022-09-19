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
    for key, value in d.items():
        if value % 2 == 1:
            print(key)
            break
    t -= 1