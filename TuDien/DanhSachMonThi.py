
class monThi:

    def __init__(self, maMon, tenMon, hinhThucThi):
        self.maMon = maMon
        self.tenMon = tenMon
        self.hinhThucThi = hinhThucThi

    def outp(self):
        return f'{self.maMon} {self.tenMon} {self.hinhThucThi}'

a = []
t = int(input())
for i in range(t):
    a.append(monThi(input(), input(), input()))

a = sorted(a, key=lambda x : x.maMon)
for i in a:
    print(i.outp())