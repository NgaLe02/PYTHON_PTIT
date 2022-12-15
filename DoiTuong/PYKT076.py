from datetime import datetime
date_format = "%d/%m/%Y"
class TheLoai:
    def __init__(self, ma, ten):
        self.ma = "TL{:03d}".format(ma)
        self.ten = ten

    def __str__(self):
        return f"{self.ma} {self.ten}"

class Phim:
    def __init__(self, ma, theLoai, ngayChieu, ten, soTap):
        self.ma = "P{:03d}".format(ma)
        self.theLoai = theLoai
        self.ngayChieu = ngayChieu
        x = ngayChieu.split('/')
        self.nam = x[2]
        self.thang = x[1]
        self.ngay = x[0]
        self.ten = ten
        self.soTap = int(soTap)
    
    def __str__(self):
        return f"{self.ma} {self.theLoai} {self.ngayChieu} {self.ten} {self.soTap}"

n, m = map(int, input().split())
a = []
for i in range(1, n + 1):
    a.append(TheLoai(i, input().strip()))

b = []
for i in range(1, m + 1):
    maTL = input().strip()
    ngay = input().strip()
    ten = input().strip()
    soTap = input().strip()
    for j in a:
        if j.ma == maTL:
            theLoai = j.ten
    b.append(Phim(i, theLoai, ngay, ten, soTap))

b = sorted(b, key=lambda x: (x.nam, x.thang, x.ngay, x.ten, -x.soTap))
print(*b, sep = "\n")

