
n = int(input())
a = [float(x) for x in input().split()]

a.sort()
minn = a[0]
maxx = a[-1]
tong = 0
b = []
for i in a:
    if i != minn and i != maxx:
        b.append(i)
        tong += i

tong /= len(b)

print('%.2f'%tong )