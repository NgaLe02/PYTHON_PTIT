
class MonHoc:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten

class CaThi:
    def __init__(self, ma, maMH, tenMH, ngayThi, gioThi, nhomThi):
        self.ma = "T{:03d}".format(ma)
        self.maMH = maMH
        self.tenMH = tenMH
        self.ngayThi = ngayThi
        self.gioThi = gioThi
        self.nhomThi = nhomThi

        x = ngayThi.split('/')
        self.ngay = x[0]
        self.thang = x[1]
        self.nam = x[2]

        x = gioThi.split(':')
        self.gio = x[0]
        self.phut = x[1]

    def __str__(self):
        return f"{self.ma} {self.maMH} {self.tenMH} {self.ngayThi} {self.gioThi} {self.nhomThi}"
n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(MonHoc(input().strip(), input().strip()))

b = []
for i in range(m):
    x = [l for l in input().strip().split()]
    for j in a:
        if j.ma == x[0]:
            tenMH = j.ten
            break

    b.append(CaThi(i + 1, x[0], tenMH, x[1], x[2], x[3]))

b = sorted(b, key=lambda x: (x.nam, x.thang, x.ngay, x.gio, x.phut, x.nhomThi))
print(*b, sep='\n')

