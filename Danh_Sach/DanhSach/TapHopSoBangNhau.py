def check(a, b):
    if len(a) != len(b):
        return 'NO'
    for i in a:
        if not i in b:
            return 'NO'
    return 'YES'

n, m = map(int, input().split())

a = set(int(x) for x in input().split())
b = set(int(x) for x in input().split())

print(check(a, b))

