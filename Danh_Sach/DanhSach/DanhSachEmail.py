
f = open("C:\\Users\\Dell E7440\\PycharmProjects\\OnTap\\DanhSach\\CONTACT.in")
lines = f.readlines()
f.close()

for i in range(len(lines)):
    lines[i] = lines[i].strip().lower()

a = list(set(lines))
a.sort()
print(*a, sep = '\n')