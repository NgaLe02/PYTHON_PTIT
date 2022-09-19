t = int(input())
while t > 0:
    l = list(str(x) for x in input().split())
    length = 0
    a = []
    for i in l:
        if length + len(i) <= 100:
            length += len(i) + 1
            a.append(i)
        else:
            break
    for i in a:
        print(i, end = ' ')
    print()
    t = t - 1