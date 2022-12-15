# Số hamming có dạng n = 2^a 3^b 5^c

N = 10 ** 18
a = []

i = 1
while i <= N:
    j = 1
    while j <= N:
        k = 1
        while k <= N:
            a.append(i * j * k)
            k *= 5
        j *= 3
    i *= 2
a.sort()

def find(l, r, x):
    if l > r:
        return 'Not in sequence'
    m = (l + r) // 2
    if a[m] == x:
        return m + 1
    if a[m] < x:
        return find(m + 1, r, x)
    return find(l, m - 1, x)

t = int(input())
while t > 0:
    n = int(input())
    print(find(0, len(a), n))
    t -= 1