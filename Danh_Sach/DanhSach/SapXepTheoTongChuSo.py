
def cmp(n):
    tong = 0
    for i in str(n):
        tong += int(i)
    return (tong, n)

t = int(input())
while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    a = sorted(a, key = cmp)
    print(*a)
    t -= 1