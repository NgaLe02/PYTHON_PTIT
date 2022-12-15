
class VT:
    def __init__(self, ten, donVi, thoiDiem):
        self.ten = ten
        self.donVi = donVi
        self.thoiDiem = thoiDiem
    
    def findMa(self):
        self.ma = ''
        for i in self.donVi.split():
            self.ma += i[0]
        for i in self.ten.split():
            self.ma += i[0]
    
    def vanToc(self):
        b = self.thoiDiem.split(':')
        x = (int(b[0]) - 6) + int(b[1]) / 60 
        self.vanToc = 120 / x

    def outp(self):
        return f"{self.ma} {self.ten} {self.donVi} {round(self.vanToc)} Km/h"
    
t = int(input())
a = []
for i in range(t):
    a.append(VT(input().strip(), input().strip(), input().strip()))
    a[-1].findMa()
    a[-1].vanToc()

a = sorted(a, key=lambda x: -x.vanToc)
for i in a:
    print(i.outp())