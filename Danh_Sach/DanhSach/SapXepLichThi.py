from datetime import datetime

class MonThi:
    def __init__(self, ma, ten, hinhThucThi):
        self.ma = ma
        self.ten = ten
        self.hinhThucThi = hinhThucThi

    def __str__(self):
        return f"{self.ma}"

class CaThi:
    def __init__(self, ma, ngay, gio, ID):
        self.ma = "C{:03d}".format(ma)
        self.time = ngay + " " + gio
        self.ngay = datetime.strptime(ngay, '%d/%m/%Y')
        self.gio = datetime.strptime(gio, "%H:%M")
        self.ID = ID
    
    def __str__(self):
        return f"{self.ma}"

class LichThi:
    def __init__(self, caThi, monThi, maNhom, soSV):
        self.caThi = caThi
        self.monThi = monThi
        self.maNhom = maNhom
        self.soSV = soSV

    def __str__(self):
        return f"{self.caThi.time} {self.caThi.ID} {self.monThi.ten} {self.maNhom} {self.soSV}"

a = []
b = []
c = []

file = open('C:\\Users\\Dell E7440\\PycharmProjects\\OnTap\\DanhSach\\MONTHI.in', 'r')
lines = file.readlines()
n = int(lines[0])
dem = 1
for i in range(n):
    a.append(MonThi(lines[dem].strip(), lines[dem + 1].strip(), lines[dem + 2].strip()))
    dem += 3

file = open('C:\\Users\\Dell E7440\\PycharmProjects\\OnTap\\DanhSach\\CATHI.in', 'r')
lines = file.readlines()
n = int(lines[0])
dem = 1
for i in range(n):
    b.append(CaThi(i + 1, lines[dem].strip(), lines[dem + 1].strip(), lines[dem + 2].strip()))
    dem += 3

file = open('C:\\Users\\Dell E7440\\PycharmProjects\\OnTap\\DanhSach\\LICHTHI.in', 'r')
lines = file.readlines()
n = int(lines[0])
dem = 1
for i in range(n):
    x = lines[dem].strip().split()
    for j in b:
        if x[0] == j.ma:
            caThi = j
            break
    for k in a:
        if x[1] == k.ma:
            monThi = k
            break
    c.append(LichThi(caThi, monThi, x[2].strip(), x[3].strip())) 
    dem += 1

c = sorted(c, key=lambda x: (x.caThi.ngay,  x.caThi.gio, x.caThi.ma))
print(*c, sep='\n')