
class GV:
    def __init__(self, maGV, tenGV, maXT, diemTH, diemCM):
        self.maGV = "GV{:02d}".format(maGV)
        self.tenGV = tenGV
        if maXT[0] == 'A':
            self.mon = 'TOAN'
        elif maXT[0] == 'B':
            self.mon = 'LY'
        elif maXT[0] == 'C':
            self.mon = 'HOA'
        self.diem= diemTH * 2 + diemCM
        
        if maXT[1] == '1':
            diemUT = 2.0
        elif maXT[1] == '2':
            diemUT = 1.5
        elif maXT[1] == '3':
            diemUT = 1.0
        else:
            diemUT = 0.0

        self.diem += diemUT

        if self.diem >= 18:
            self.trangThai = 'TRUNG TUYEN'
        else:
            self.trangThai = 'LOAI'


    def __str__(self):
        return f"{self.maGV} {self.tenGV} {self.mon} {format(self.diem, '.1f')} {self.trangThai}"

t = int(input())
a = []
for i in range(1, t + 1):
    a.append(GV(i, input().strip(), input().strip(), float(input().strip()), float(input())))

a = sorted(a, key=lambda x : -x.diem)
print(*a, sep='\n')