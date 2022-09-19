class HoaDon:
    def __init__(self, ma, tenKH, chiSoCu, chiSoMoi):
        self.tenKH  =tenKH
        self.chiSoCu = chiSoCu
        self.chiSoMoi = chiSoMoi
        self.maKH = "KH{:02d}".format(ma)
        self.tongTien = 0

    def set(self):
        x = self.chiSoMoi - self.chiSoCu
        if x <= 50:
            self.tongTien = int(round(x * 100 * 1.02, 0))
        elif x <= 100:
            self.tongTien = int(round((50 * 100 + (x - 50) * 150) * 1.03, 0))
        elif x > 100:
            self.tongTien = int(round((50 * 100 + 50 * 150 + (x - 100) * 200)* 1.05, 0))

    def __str__(self):
        return f"{self.maKH} {self.tenKH} {self.tongTien}"


n = int(input())
a = []
for i in range(n):
    a.append(HoaDon(i + 1, input(), int(input()), int(input())))
    a[i].set()

a.sort(key=lambda x: x.tongTien, reverse=True)
for i in a:
    print(i)