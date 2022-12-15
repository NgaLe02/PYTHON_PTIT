
t = int(input())
while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for key, val in d.items():
        if val % 2 == 1:
            print(key)
            break
    t -= 1