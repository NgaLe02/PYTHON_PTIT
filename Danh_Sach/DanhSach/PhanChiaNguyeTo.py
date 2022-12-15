import math
def snt(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

n = int(input())
a = []
res = []
sum = 0
for x in input().split():
    if not int(x) in a:
        a.append(int(x))
        sum += int(x)
        res.append(sum)

ok = 0
for i in range(len(a)):
    if snt(res[i]) and snt(sum - res[i]):
        print(i)
        ok = 1
        break
if ok == 0:
    print('NOT FOUND')

