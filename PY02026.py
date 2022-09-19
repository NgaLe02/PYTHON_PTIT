def check(a, b):
    if len(a) != len(b):
        return 0
    for i in range (len(a)):
        if a[i] != b[i]:
            return 0
    return 1

n, m = [int(x) for x in input().split()]

a = list(set(int(x) for x in input().split()))
b = list(set(int(x) for x in input().split()))
a.sort()
b.sort()
if check(a, b):
    print('YES')
else:
    print('NO')