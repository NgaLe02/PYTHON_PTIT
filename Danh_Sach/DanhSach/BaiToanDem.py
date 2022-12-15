
n = int(input())
a = []

while True:
    for x in input().split():
        a.append(int(x))
    if len(a) == n:
        break

dem = 0
m = a[-1]
ok = 0
for i in range(1, m + 1):
    if not i in a:
        print(i)
        ok = 1
if ok == 0:
    print('Excellent!')

