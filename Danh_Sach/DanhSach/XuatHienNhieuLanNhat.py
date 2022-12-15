
t = int(input())
while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else: 
            d[i] = 1

    num = 0
    times = 0 
    for key, value in d.items():
        if value > times:
            times = value
            num = key

    if times > n // 2:
        print(num)
    else:
        print('NO')
    t -= 1