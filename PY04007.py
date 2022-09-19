class Matrix:
    def __init__(self, n, m , a):
        self.m = m
        self.n = n
        self.a = a

    def mul(self):
        for i in range(self.n):
            for j in range(self.n):
                x = 0
                for k in range(self.m):
                    x += (self.a[i][k] * self.a[j][k])
                print(x, end = " ")
            print()


t = int(input())
while t > 0:
    n, m = map(int,input().split())
    a = []
    for i in range(n):
        a.append([int(i) for i in input().split()])
    matran = Matrix(n, m, a)
    matran.mul()
    t -= 1