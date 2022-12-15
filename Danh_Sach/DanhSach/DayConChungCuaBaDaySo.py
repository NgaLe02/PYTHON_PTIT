
def solve():
    n, m, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    check = False
    i = 0
    j = 0
    l = 0
    while i < n and j < m and l < k:
        if a[i] == b[j] == c[l]:
            print(a[i], end = " ")
            check = True
            i += 1
            j += 1
            l += 1
            continue
        if a[i] < b[j] or a[i] < c[l]:
            i += 1
            continue
        if b[j] < a[i] or b[j] < c[l]:
            j += 1
            continue
        if c[l] < a[i] or c[l] < b[j]:
            l += 1
            continue
    if check == False:
        print('NO', end = ' ')
    print()

t = int(input())
while t > 0:
    solve()
    t -= 1