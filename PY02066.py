n = int(input())
a = []
while True:
    a.extend(int(x) for x in input().split())
    if len(a) == n:
        break
maxx = a[len(a) - 1]
check = 0
for i in range (1, maxx + 1):
    if not(i in a):
        check = 1
        print(i)
if check == 0:
    print("Excellent!")