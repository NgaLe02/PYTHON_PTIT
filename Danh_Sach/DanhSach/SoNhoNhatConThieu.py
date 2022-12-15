
n = int(input())
a = [int(x) for x in input().split()]
a.sort()
ok = 0
for i in range(1, n + 1):
    if not i in a:
        print(i)
        ok = 1
        break
if ok == 0:
    print(n + 1)