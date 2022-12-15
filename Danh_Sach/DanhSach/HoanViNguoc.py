from itertools import permutations

t = int(input())
while t > 0:
    n = int(input())
    a = []
    for i in range(n, 0, -1):
        a.append(i)
    dem = 0
    s = permutations(a)
    for i in s:
        dem += 1
    print(dem)
    x = permutations(a)
    for i in x:
        print(*i, sep='', end = ' ')
    print()
    t -= 1