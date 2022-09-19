list = []
while True:
    for x in input().split():
        list.append(int(x))
    if len(list) == 10:
        break

tmp = []
for i in range (0, 10):
    x = list[i] % 42
    if tmp.count(x) == 0:
        tmp.append(x)
print(len(tmp))