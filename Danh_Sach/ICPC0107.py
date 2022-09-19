def tnn():
    a = str(min(p, q))
    b = str(max(p, q))
    y1 = x1.replace(b, a)
    y2 = x2.replace(b, a)
    return int(y1) + int(y2)

def tln():
    a = str(min(p, q))
    b = str(max(p, q))
    y1 = x1.replace(a, b)
    y2 = x2.replace(a, b)
    return int(y1) + int(y2)

t = int(input())
while t > 0:
    p, q = [str(x) for x in input().split()]
    list = []
    while True:
        for x in input().split():
            list.append(str(x))
        if len(list) == 2:
            break
    x1 = list[0]
    x2 = list[1]
    print(f"{tnn()} {tln()}")
    t -= 1