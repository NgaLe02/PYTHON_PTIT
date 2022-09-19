
t = int(input())
while t > 0:
    n = int(input())
    list = []
    while True:
        list.append(int(input()))
        if len(list) == n:
            break
    mem = 0
    count = 0
    for i in range (n):
        tmp = list.count(list[i])
        if tmp > count:
            mem = list[i]
            count = tmp
        elif tmp == count:
            mem = min(list[i], mem)
    print(mem)
    t -= 1