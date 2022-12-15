
from datetime import datetime

class caThi:
    def __init__(self, ma, ngay, gio, phong):
        self.ma = "C{:03d}".format(ma)
        self.time = ngay + " " + gio
        self.ngay = datetime.strptime(ngay, '%d/%m/%Y')
        self.gio = datetime.strptime(gio, "%H:%M")
        self.phong = phong
    
    def __str__(self):
        return f"{self.ma} {self.time} {self.phong}"

f = open('C:\\Users\\Dell E7440\\PycharmProjects\\OnTap\\DanhSach\\CATHI.in', 'r')
lines = f.readlines()
a = []
dem = 1
for i in range(1, len(lines), 3):
    a.append(caThi(dem, lines[i].strip(), lines[i + 1].strip(), lines[i + 2].strip()))
    dem += 1
a = sorted(a, key=lambda x:(x.ngay, x.gio, x.ma))

for i in a:
    print(i)
