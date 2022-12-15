l = []
while True:
    s = input()
    for x in s.split():
        l.append(int(x))
    if len(l) == 10:
        break

for i in range(len(l)):
    l[i] %= 42
l = set(l)
print(len(l))