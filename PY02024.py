def cmp(n):
    tich = 1
    n = str(n)
    for i in n:
        tich *= int(i)
    return (tich, int(n))


t = int(input())

while t > 0:
    n = int(input())
    l = [int(x) for x in input().split()]
    l_new = sorted(l, key = cmp)
    for i in l_new:
        print(i, end = ' ')
    print()
    t -= 1