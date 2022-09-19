
class soPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao

    def add(self, s):
        return soPhuc(self.thuc + s.thuc, self.ao + s.ao)

    def mul(self, s):
        x = self.thuc * s.thuc - self.ao * s.ao
        y = self.thuc * s.ao + self.ao * s.thuc
        return soPhuc(x, y)

    def show(self):
        x = ''
        if self.ao >= 0:
            x = "+"
        else:
            x = '-'
        self.ao = abs(self.ao)
        return f"{self.thuc} {x} {self.ao}i"


t = int(input())
while t > 0:
    arr = input().split()
    s1 = soPhuc(int(arr[0]), int(arr[1]))
    s2 = soPhuc(int(arr[2]), int(arr[3]))
    s = s1.add(s2)
    c = s.mul(s1)
    d = s.mul(s)
    print(c.show(), end = ', ')
    print(d.show())
    t -= 1