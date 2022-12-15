
l = []
l.append(0)
l.append(1)
l.append(1)

for i in range(3, 93):
    l.append(l[i- 1] + l[i - 2])

t = int(input())
while t > 0:
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        print(l[i], end = ' ')
    print()
    t -= 1
