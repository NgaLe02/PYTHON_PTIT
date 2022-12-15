

class HD:
    def __init__(self, maMH, tenMH, soLuong, donGia, tienCK):
        self.maMH = maMH
        self.tenMH = tenMH
        self.soLuong = soLuong
        self.donGia = donGia
        self.chietKhau = tienCK
        self.tong = donGia * soLuong - tienCK
    
    def __str__(self):
        return f"{self.maMH} {self.tenMH} {self.soLuong} {self.donGia} {self.chietKhau} {self.tong}"

t = int(input())
a = []
for i in range (1, t + 1):
    a.append(HD(input().strip(), input().strip(), int(input()), int(input()), int(input())))

a = sorted(a, key=lambda x: -x.tong)
print(*a, sep = '\n')