
t = int(input())
while t > 0:
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    maxx = max(a)
    for i in range(len(a)):
        if a[i] == maxx:
            a.insert(i, m)
            break
    for i in a:
        if i < 0:
            print(i, end = ' ')
    for i in a:
        if i >= 0:
            print(i, end = ' ')
    print()
    t -= 1