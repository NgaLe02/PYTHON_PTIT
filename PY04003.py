import math


class phanSo:
    def __init__(self, tuSo, mauSo):
        self.tuSo = tuSo;
        self.mauSo = mauSo;

    def rutGon(self):
        x = math.gcd(self.tuSo, self.mauSo)
        return str(self.tuSo // x) + "/" + str(self.mauSo//x)


arr = input().split()
p = phanSo(int(arr[0]), int(arr[1]))
print(p.rutGon())

