def check(a, b, n):
    a.sort()
    b.sort()
    for i in range(n):
        if a[i] > b[i]:
            return 'NO'
    return 'YES'

t = int(input())
while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(check(a, b, n))
    t -= 1