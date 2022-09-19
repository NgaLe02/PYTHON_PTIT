import datetime


class HoaDon:
    def __init__(self, x, ten, sophong, ngayNhan, ngayTra, tienDichVu):
        self.maKH = "KH{:02d}".format(x)
        self.ten = ten
        self.soPhong = sophong
        self.ngayNhanPhong = ngayNhan
        self.ngayTraPhong = ngayTra
        self.tienDichVu = tienDichVu
        self.thanhtien = 0
        self.songayo = 0

    def _set_so_ngay_o(self):
        t = datetime.datetime.strptime(self.ngayNhanPhong, '%d/%m/%Y')
        t1 = datetime.datetime.strptime(self.ngayTraPhong, '%d/%m/%Y')
        self.songayo = (t1 - t).days + 1

    def _set_thanh_tien(self):
        gia = 0
        if self.soPhong[0] == '1':
            gia = 25
        elif self.soPhong[0] == '2':
            gia = 34
        elif self.soPhong[0] == '3':
            gia = 50
        elif self.soPhong[0] == '4':
            gia = 80
        self.thanhtien = self.songayo * gia + self.tienDichVu

    def __str__(self):
        return f"{self.maKH} {self.ten} {self.soPhong} {self.songayo} {self.thanhtien}"


n = int(input())
a = []
for i in range(n):
    a.append(HoaDon(i + 1, input(), input(), input(), input(), int(input())))
    a[i]._set_so_ngay_o()
    a[i]._set_thanh_tien()

a.sort(key=lambda x: x.thanhtien, reverse=True)

for x in a:
    print(x)