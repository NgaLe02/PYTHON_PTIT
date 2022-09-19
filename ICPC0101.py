n = int(input())

l = [int(x) for x in input().split()]
res = []

for i in l:
    if len(res) == 0:
        res.append(i)
    else :
        if (res[-1] + i) % 2 == 0:
            res.pop()
        else :
            res.append(i)
print(len(res))


