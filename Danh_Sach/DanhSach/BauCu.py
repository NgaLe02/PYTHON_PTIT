
n, m = map(int, input().split())
a = [int(x) for x in input().split()]

d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

b = []
for val in d.values():
    b.append(val)
b = sorted(b, reverse=True)
second = b[0]
for i in b:
    if i != second:
        second = i
        break
if second == b[0]:
    print('NONE')
else:
    for key in d.keys():
        if d[key] == second:
            print(key)
            break

