t = int(input())

while t > 0:
    n, d = [int(x) for x in input().split()]
    list = input().split()
    for i in range(d, len(list)):
        print(list[i], end = " ")
    for i in range(0, d):
        print(list[i], end = ' ')
    print()
    t -= 1