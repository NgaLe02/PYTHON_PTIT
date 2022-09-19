class XepHang:
    def __init__(self, ten, ac, sb):
        self.ten = ten
        self.ac = ac
        self.submit = sb

    def __str__(self):
        return f"{self.ten} {self.ac} {self.submit}"


n = int(input())

a = []
for i in range(n):
    s = input()
    ac, sb = map(int, input().split())
    a.append(XepHang(s, ac, sb))

a.sort(key=lambda x: (-x.ac, x.submit, x.ten), reverse=False)

for i in a:
    print(i)