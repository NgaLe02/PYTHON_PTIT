class LuongMua:
    def __init__(self, ma, tenTram, thoiDiemBatDauMua, thoiDiemKetThucMua, luongMua):
        self.ma = "T{:02d}".format(ma)
        self.tenTram = tenTram
        self.thoiDiemBatDauMua = thoiDiemBatDauMua
        self.thoiDiemKetThucMua = thoiDiemKetThucMua
        self.luongMua = luongMua
        self.thoiGian = 0
        self.luongMuaTB = 0

    def setthoigian(self, thoiDiemBatDau, thoiDiemKetThuc):
        t = list(int(x) for x in thoiDiemBatDau.split(":"))
        t1 = list(int(x) for x in thoiDiemKetThuc.split(":"))
        self.thoiGian += (t1[0] * 60 + t1[1]) - (t[0] * 60 + t[1])

    def setluongmua(self, luongMua):
        self.luongMua += luongMua

    def setluongmuatb(self):
        t = float(self.thoiGian / 60)
        self.luongMuaTB = float(self.luongMua / t)

    def __str__(self):
        x = format(self.luongMuaTB, ".2f")
        return f"{self.ma} {self.tenTram} {x}"


t = int(input())
se = []
a = []
for i in range(t):
    tenTram = input()
    t1 = input()
    t2 = input()
    luongMua = float(input())
    if not(tenTram in se):
        se.append(tenTram)
        a.append(LuongMua(i + 1, tenTram, t1, t2, luongMua))
        a[-1].setthoigian(t1, t2)
    else:
        for x in a:
            if x.tenTram == tenTram:
                x.setthoigian(t1, t2)
                x.setluongmua(luongMua)

for x in a:
    x.setluongmuatb()
    print(x)