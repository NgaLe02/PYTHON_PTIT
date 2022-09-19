class Tuyen:
    def __init__(self, ma, ten, diemLT, diemTH):
        self.ma = "TS{:02d}".format(ma)
        self.ten = ten
        self.diemTB = (diemTH + diemLT) / 2
        self.xepLoai = ''

    def setxeploai(self):
        if self.diemTB < 5:
            self.xepLoai = 'TRUOT'
        elif self.diemTB < 8:
            self.xepLoai = 'CAN NHAC'
        elif self.diemTB < 9.5:
            self.xepLoai = 'DAT'
        else:
            self.xepLoai = 'XUAT SAC'

    def __str__(self):
        self.diemTB = format(self.diemTB, ".2f")
        return f"{self.ma} {self.ten} {self.diemTB} {self.xepLoai}"


n = int(input())
a = []
for i in range(n):
    s = input()
    d1 = float(input())
    d2 = float(input())
    if d1 > 10:
        d1 = d1 / 10
    if d2 > 10:
        d2 = d2 / 10
    a.append(Tuyen(i + 1, s, d1, d2))
    a[i].setxeploai()

a.sort(key=lambda x: x.diemTB, reverse=True)

for i in a:
    print(i)