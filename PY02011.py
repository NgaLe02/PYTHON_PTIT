n = int(input())
a = list(int(x) for x in input().split())

minn = 10000000
mem = 0
for i in range (n):
    sum = 0
    for j in range (n):
        sum += abs(a[i] - a[j])
    if sum < minn:
        minn = sum
        mem = a[i]
print(f"{minn} {mem}")