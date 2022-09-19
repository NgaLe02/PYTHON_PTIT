
t = int(input())
while t > 0:
    n = int(input())
    a = list(set(int(x) for x in input().split()))
    a.sort()
    dem = 0
    print(a)
    for i in range (0, len(a) - 1):
        dem += a[i + 1] - a[i] - 1
    print(dem)
    t = t - 1