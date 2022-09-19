n, m = [int(x) for x in input().split()]

a = set(int(x) for x in input().split())
b = set(int(x) for x in input().split())

intersectionn = list(a.intersection(b))
subAB = list(a.difference(b))
subBA = list(b.difference(a))

intersectionn.sort()
subAB.sort()
subBA.sort()

for  i in intersectionn:
    print(i, end = ' ')
print()
for  i in subAB:
    print(i, end = ' ')
print()
for  i in subBA:
    print(i, end = ' ')
print()