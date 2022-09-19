n = int(input())
list = [float(x) for x in input().split()]

list.sort()
min = list[0]
max = list[n - 1]
while min in list:
   list.remove(min)
while max in list:
   list.remove(max)
tong = float(0)
for i in list:
    tong += i
print("{:.2f}".format(tong / len(list)) )
