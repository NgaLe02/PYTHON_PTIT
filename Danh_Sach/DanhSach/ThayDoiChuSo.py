
def solve(x1, x2, minn, maxx):
    t1 = x1
    t2 = x2
    t1 = t1.replace(maxx, minn)
    t2 = t2.replace(maxx, minn)
    tnn = int(t1) + int(t2)
    print(tnn, end = ' ')
    x1 = x1.replace(minn, maxx)
    x2 = x2.replace(minn, maxx)
    tln = int(x1) + int(x2)
    print(tln)

t = int(input())
while t > 0:
    p, q = map(int, input().split())
    list = []
    while True:
        for x in input().split():
            list.append(str(x))
        if len(list) == 2:
            break
    x1 = list[0]
    x2 = list[1]
    maxx = str(max(p, q))
    minn = str(min(p, q))
    solve(x1, x2, minn, maxx)
    t -= 1