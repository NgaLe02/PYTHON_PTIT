
lines1 = open('C:\\Users\\Dell E7440\\PycharmProjects\\OnTap\\DanhSach\\DATA1.in', 'r')
lines2 = open('C:\\Users\\Dell E7440\\PycharmProjects\\OnTap\\DanhSach\\DATA2.in', 'r')

s1 = []
for i in lines1:
    for j in i.strip().lower().split():
        s1.append(j)

s2 = []
for i in lines2:
    for j in i.strip().lower().split():
        s2.append(j)

s1 = set(s1)
s2 = set(s2)


c = list(s1.difference(s2))
c.sort()
print(*c)
c = list(s2.difference(s1))
c.sort()
print(*c)

