s = input()
tong = 0
while True:
    n = len(s) // 2
    a = int(s[:n])
    b = int(s[n:])
    c = a + b
    print(c)
    if c < 10:
        break
    s = str(c)

