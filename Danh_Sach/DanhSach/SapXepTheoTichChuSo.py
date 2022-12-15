def cmp(n):
    tich = 1
    for i in str(n):
        tich *= int(i)
    return (tich, n)

t = int(input())
while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    a = sorted(a, key = cmp)
    print(*a)
    t -= 1