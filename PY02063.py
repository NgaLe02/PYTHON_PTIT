n = int(input())

a = list(int(x) for x in input().split())

a.sort(reverse= True)
#3 so dau duong
max1 = a[0] * a[1] * a[2]
#1 so dau duong, 2 so cuoi am
max2 = a[0] * a[len(a) - 1] * a[len(a) - 2]
#2 so dau duong
max3 = a[0] * a[1]
#2 so cuoi am
max4 = a[len(a) - 1] * a[len(a) - 2]
print(max(max4, max3, max2, max1))