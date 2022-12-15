
n, m = map(int, input().split())
a = set(int(x) for x in input().split())
b = set(int(x) for x in input().split())

x = list(a.intersection(b))
x.sort()
y = list(a.difference(b))
y.sort()
z = list(b.difference(a))
z.sort()

print(*x)
print(*y)
print(*z)


