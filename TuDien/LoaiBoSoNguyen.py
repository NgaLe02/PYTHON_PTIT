
f = open("C:\\Users\\Dell E7440\\PycharmProjects\\OnTap\\TuDien\\DATA.in", "r")
s = f.readlines()

a = []
for i in s:
    i = i.strip()
    for j in i.split():
        if not j.isdigit():
           a.append(j)
        elif int(j) > 2147483647:
            a.append(j)

a.sort()
print(*a)