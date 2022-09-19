def doi(l):
    if 39 <= l <= 40:
        return 9
    if 37 <= l <= 38:
        return 8.5
    if 35 <= l <= 36:
        return 8
    if 33 <= l <= 34:
        return 7.5
    if 30 <= l <= 32:
        return 7
    if 27 <= l <= 29:
        return 6.5
    if 23 <= l <= 26:
        return 6
    if 20 <= l <= 22:
        return 5.5
    if 16 <= l <= 19:
        return 5
    if 13 <= l <= 15:
        return 4.5
    if 10 <= l <= 12:
        return 4
    if 7 <= l <= 9:
        return 3.5
    if 5 <= l <= 6:
        return 3.0
    if 3 <= l <= 4:
        return 2.5


t = int(input())
while t > 0:
    a = [str(x) for x in input().split()]
    r = int(a[0])
    l = int(a[1])
    s = float(a[2])
    w = float(a[3])

    score = (doi(r) + doi(l) + s + w) / 4.0
    if score - int(score) >= 0.75:
        print(float(int(score)) + 1.0)
    elif score - int(score) >= 0.25:
        print(float(int(score)) + 0.5)
    else:
        print(float(int(score)))
    t -= 1

