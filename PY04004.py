import math


class phanSo:
    def __init__(self, tuSo, mauSo):
        self.tuSo = tuSo;
        self.mauSo = mauSo;

    def rutGon(self):
        x = math.gcd(self.tuSo, self.mauSo)
        return phanSo(self.tuSo//x, self.mauSo//x)

    def add(self, p):
        x = self.tuSo * p.mauSo + p.tuSo * self.mauSo
        y = self.mauSo * p.mauSo
        tmp = phanSo(x, y).rutGon()
        return f"{tmp.tuSo}/{tmp.mauSo}"


arr = input().split()
p1 = phanSo(int(arr[0]), int(arr[1]))
p2 = phanSo(int(arr[2]), int(arr[3]))
p1 = p1.rutGon()
p2 = p2.rutGon()
print(p1.add(p2))


