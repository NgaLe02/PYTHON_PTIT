class thiSinh:
    def __init__(self, ten, ns, diem1, diem2, diem3):
        self.ten = ten
        self.ns = ns
        self.tongDiem = diem1 + diem2 + diem3

    def inp(self):
        return self.ten + " " + self.ns + " " + format(self.tongDiem, ".1f")
ten = input()
ngaySinh = input()
diem1 = float(input())
diem2 = float(input())
diem3 = float(input())
t = thiSinh(ten, ngaySinh, diem1, diem2, diem3)
print(t.inp())


