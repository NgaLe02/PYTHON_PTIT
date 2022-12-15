
def chuanHoaTen(s):
    x = s.strip().lower().split()
    s = ''
    for i in x:
        s += i[0].upper() + i[1:] + " "
    return s.strip()

class SV:
    def __init__(self, ma, ten, diem):
        self.ma = "SV{:02d}".format(ma)
        self.ten = ten
        self.diem = diem
        self.rank = None
    

    def __str__(self):
        self.diem = format(self.diem, '.2f')
        return f"{self.ma} {self.ten} {self.diem} {self.rank}"
    
n = int(input())
a = []
for i in range(n):
    ten = chuanHoaTen(input())
    diem1 = float(input())
    diem2 = float(input())
    diem3 = float(input())
    diem = (diem1 * 3 + diem2 * 3 + diem3 * 2) / 8 + 0.001
    a.append(SV(i + 1, ten, diem))

a = sorted(a, key=lambda x: -x.diem)
a[0].rank = 1
for i in range(1, n):
    if a[i].diem == a[i - 1].diem:
        a[i].rank = a[i - 1].rank
    else:
        a[i].rank = i + 1

print(*a, sep='\n')