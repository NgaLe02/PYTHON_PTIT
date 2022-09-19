
n = int(input())
list = []
while True:
    for x in input().split():
        list.append(int(x))
    if len(list) == n:
        break

even = []
odd = []
mark = []
for i in list:
    if i % 2 == 0:
        even.append(i)
        mark.append(0)
    else:
        odd.append(i)
        mark.append(1)
even2 = sorted(even)
ood2 = sorted(odd, reverse = True)
chan = 0
le = 0
for i in mark:
    if i == 0:
        print(even2[chan], end = ' ')
        chan += 1
    else:
        print(ood2[le], end = ' ')
        le += 1

