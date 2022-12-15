
def chuanHoaTen(s):
    s = s.lower().strip()
    x = s.split()
    s = ''
    for i in x:
        s += i[0].upper() + i[1:] + ' '
    return s.strip()

class KH:
    def __init__(self, ma, hoTen, loaiHGD, chiSD, chiSC):
        self.ma = "KH{:02d}".format(ma)
        self.hoTen = hoTen
        self.loaiHGD = loaiHGD
        self.chiSD = chiSD
        self.chiSC = chiSC
    
    def _tinhTien(self):
        dinhMuc = 0
        if self.loaiHGD == 'A':
            dinhMuc = 100
        elif self.loaiHGD == 'B':
            dinhMuc = 500
        else:
            dinhMuc = 200
        x = self.chiSC - self.chiSD
        if x < dinhMuc:
            self.tienTrongDM = x * 450
            self.tienVuotDM = 0
            self.thue = self.tienVuotDM // 20
        else:
            self.tienTrongDM = dinhMuc * 450
            self.tienVuotDM = (x - dinhMuc) * 1000
            self.thue = self.tienVuotDM // 20
        
        self.tongTien = self.tienTrongDM + self.tienVuotDM + self.thue
        

    def __str__(self):
        return f"{self.ma} {self.hoTen} {self.tienTrongDM} {self.tienVuotDM} {self.thue} {self.tongTien}"
a = []
t = int(input())
for i in range(t):
    x1 = chuanHoaTen(input())
    x2 = input().strip().split()
    a.append(KH(i + 1, x1, x2[0], int(x2[1]), int(x2[2])))
    a[-1]._tinhTien()

a = sorted(a, key=lambda x: -x.tongTien)
print(*a, sep='\n')
