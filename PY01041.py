def check(n):
    dem = 0
    r = n % 10
    n = int(n / 10)
    ok = 0
    while n > 0:
        dem += 1
        l = n % 10
        if ok == 0 and l < r:
            ok = 1
        elif ok == 0 and l == r:
            return 0
        elif ok == 1 and l >= r:
            return 0
        r = l
        n = int(n / 10)
    if dem >= 3:
        return 1
    else:
        return 0

t = int(input())
while t > 0:
    n = int(input())
    if check(n) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1