
t = int(input())
while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    l = max(a)
    r = min(a)
    dem = 0
    for i in range(r, l + 1):
        if not i in a:
            dem += 1
    print(dem)
    t -= 1