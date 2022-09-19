def soDao(n):
    m = 0
    while n > 0:
        m = m * 10 + n % 10
        n = int(n / 10)
    return m

def usc(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
t = int(input())
while t > 0:
    n = int(input())
    m = soDao(n)
    if (usc(n, m) == 1):
        print("YES")
    else:
        print("NO")
    t -= 1