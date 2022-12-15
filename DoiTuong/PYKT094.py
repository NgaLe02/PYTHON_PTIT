
d = {
    ('A', (1, 3)) : 10,
    ('A', (4, 8)) : 12,
    ('A', (9, 15)) : 14,
    ('A', (16, 100)) : 20,
    ('B', (1, 3)) : 10,
    ('B', (4, 8)) : 11,
    ('B', (9, 15)) : 13,
    ('B', (16, 100)) : 16,
    ('C', (1, 3)) : 9,
    ('C', (4, 8)) : 10,
    ('C', (9, 15)) : 12,
    ('C', (16, 100)) : 14,
    ('D', (1, 3)) : 8,
    ('D', (4, 8)) : 9,
    ('D', (9, 15)) : 11,
    ('D', (16, 100)) : 13,
}

class PhongBan:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten

class NhanVien:
    def __init__(self, ma, ten, phongBan, luongCB, soNC):
        self.ma = ma
        self.ten = ten
        self.phongBan = phongBan
        self.luongCB = luongCB
        self.soNC = soNC

    def _luong_(self):
        phanLoai = ma[0]
        # print(phanLoai)
        soNamCT = int(ma[1:3])
        # print(soNamCT)
        for i in d.items():
            if phanLoai == i[0][0]:
                if i[0][1][0] <= soNamCT <= i[0][1][1]:
                    heSoNhan = i[1]
        self.luong = self.luongCB * self.soNC * heSoNhan * 1000

    def __str__(self):
        return f"{self.ma} {self.ten} {self.phongBan} {self.luong}"
n  = int(input())
a = []
for i in range (n):
    s = input().strip().split(" ", 1)
    a.append(PhongBan(s[0], s[1]))

m = int(input())
b = []
for i in range(m):
    ma = input()
    ten = input()
    luongCB = int(input())
    soNC = int(input())
    for j in a:
        if j.ma == ma[3:5]:
            phongBan = j.ten
            break
    b.append(NhanVien(ma, ten, phongBan, luongCB, soNC))
    b[-1]._luong_()


print(*b, sep='\n')