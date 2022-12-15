def solve(a, n):

    dem = 0
    for i in range (0, n - 2):
        l = i + 1
        k = n - 1
        while l < k:
            if a[i] + a[l] + a[k] == 0:
                l += 1
                dem += 1
            elif a[i] + a[l] + a[k] > 0:
                k -= 1
            else:
                l += 1
    print(dem)

t = int(input())

while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    solve(a, n)
    t -= 1