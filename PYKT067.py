from itertools import permutations

t = int(input())

while t > 0:
    n = int(input())
    a = []
    for i in range (n, 0, -1):
        a.append(i)
    s = permutations(a)
    dem = 0
    x = permutations(a)
    for i in x:
        dem += 1
    print(dem)
    for i in s:
        print(*i, sep = '', end = ' ')
    print()
    t -= 1