class SinhVien:
    def __init__(self, maSV, ten, lop):
        self.maSV = maSV
        self.ten = ten
        self.lop = lop
        self.diemCC = 0
        self.ghiChu = ''

    def setdiemCC(self, s):
        diem = 10
        for i in s:
            if i == 'm':
                diem -= 1
            elif i == 'v':
                diem -= 2
        if diem < 0:
            diem = 0
        self.diemCC = diem

    def setghichu(self):
        if self.diemCC == 0:
            self.ghiChu = 'KDDK'

    def __str__(self):
        if self.ghiChu == '':
            return f"{self.maSV} {self.ten} {self.lop} {self.diemCC}"
        else:
            return f"{self.maSV} {self.ten} {self.lop} {self.diemCC} {self.ghiChu}"


n = int(input())
a = []
for i in range(n):
    a.append(SinhVien(input(), input(), input()))

for i in range(n):
    x, y = map(str, input().split())
    for j in a:
        if j.maSV == x:
            j.setdiemCC(y)
            j.setghichu()
            break

for i in a:
    print(i)
