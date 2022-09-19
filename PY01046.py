def chuyen(n, a, b):
    print(f"{a} -> {b}")
def thapHN(n, a, b, c):
    if n == 1:
        chuyen(1, a, c)
        return
    thapHN(n - 1, a, c, b)
    chuyen(n, a, c)
    thapHN(n - 1, b, a, c)

n = int(input())
thapHN(n, 'A', 'B', 'C')