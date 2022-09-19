
def check(a, b, n):
    for i in range (0, n):
        if a[i] > b[i]:
            return 0
    return 1

t = int(input())
while t > 0:
    n = int(input())
    a = list(int(x) for x in input().split())
    b = list(int(x) for x in input().split())
    a.sort()
    b.sort()
    if check(a,b,n):
        print('YES')
    else:
        print('NO')
    t = t - 1