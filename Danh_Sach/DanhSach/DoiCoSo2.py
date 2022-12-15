s = "0123456789ABCDEF"

def base4(x):
    num = ''
    for i in range(0, len(x), 2):
        tmp = 0
        if x[i] == '1':
            tmp += 2
        if x[i + 1] == '1':
            tmp += 1
        num = num + str(tmp)
    return num

def base8(x):
    num = ''
    for i in range(0, len(x), 3):
        tmp = 0
        if x[i] == '1':
            tmp += 4
        if x[i + 1] == '1':
            tmp += 2
        if x[i + 2] == '1':
            tmp += 1
        num = num + str(tmp)
    return num

def base16(x):
    num = ''
    for i in range(0, len(x), 4):
        tmp = 0
        if x[i] == '1':
            tmp += 8
        if x[i + 1] == '1':
            tmp += 4
        if x[i + 2] == '1':
            tmp += 2
        if x[i + 3] == '1':
            tmp += 1
        num = num + s[tmp]
    return num

def solve(x, b):
    if b == 2:
        return x
    if b == 4: l = 2
    elif b == 8: l = 3
    elif b == 16: l = 4

    while len(x) % l != 0:
        x = '0' + x
    if b == 4:
        return base4(x)
    if b == 8:
        return base8(x)
    if b == 16:
        return base16(x)

t = int(input())
while t > 0:
    b = int(input())
    x = input()
    print(solve(x, b))
    t -= 1