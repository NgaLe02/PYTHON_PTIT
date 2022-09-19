while True:
    n = int(input())
    if n == 0:
        break
    a = []
    while n > 0:
        a.append(int(input()))
        n = n - 1
    a.sort()
    if a[0] == a[n - 1]:
        print('BANG NHAU')
    else:
        print(f"{a[0]} {a[n - 1]}")