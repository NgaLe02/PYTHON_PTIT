

class bangDiem:
    def __init__(self, ma, hoTen, diemTB):
        self.ma = "HS{:02d}".format(ma)
        self.hoTen = hoTen
        self.diemTB = round(diemTB / 10 / 1.2, 1)
        self.xepLoai = ""

    def setXepLoai(self):
        if self.diemTB >= 9:
            self.xepLoai = "XUAT SAC"
        elif self.diemTB >= 8:
            self.xepLoai = "GIOI"
        elif self.diemTB >= 7:
            self.xepLoai = "KHA"
        elif self.diemTB >= 5:
            self.xepLoai = "TB"
        else:
            self.xepLoai = 'YEU'

    def __repr__(self):
        self.diemTB = format(self.diemTB, '.1f')
        return f"{self.ma} {self.hoTen} {self.diemTB} {self.xepLoai}"


n = int(input())
a = []
for i in range (0, n):
    s = input()
    b = list(float(x) for x in input().split())
    cnt = 0
    cnt += b[0] * 2 + b[1] * 2
    for j in range (2, 10):
        cnt += b[j]
    a.append(bangDiem(i + 1, s, cnt))

for i in a:
    i.setXepLoai()

a.sort(key=lambda x: (-x.diemTB, x.ma), reverse=False)

for i in a:
    print(i)

