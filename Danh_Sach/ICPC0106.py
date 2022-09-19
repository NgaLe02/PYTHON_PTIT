p = "ABCDEF"
def base4(s):
    num = ''
    for i in range (0, len(s), 2):
        tmp = 0
        if s[i] == '1':
            tmp += 2
        if s[i + 1] == '1':
            tmp += 1
        num = num + str(tmp)
    return num

def base8(s):
    num = ''
    for i in range (0, len(s), 3):
        tmp = 0
        if s[i] == '1':
            tmp += 4
        if s[i + 1] == '1':
            tmp += 2
        if s[i + 2] == '1':
            tmp += 1
        num = num + str(tmp)
    return num

def base16(s):
    num = ''
    for i in range (0, len(s), 4):
        tmp = 0
        if s[i] == '1':
            tmp += 8
        if s[i + 1] == '1':
            tmp += 4
        if s[i + 2] == '1':
            tmp += 2
        if s[i + 3] == '1':
            tmp += 1
        if tmp <= 9:
            num = num + str(tmp)
        else:
            num = num + p[tmp - 10]
    return num

def solve(n, b):
    if b == 2:
        return n;
    if b == 4:
        l = 2
    elif b == 8:
        l = 3
    else:
        l = 4
    while len(n) % l != 0:
        n = '0' + n
    if b == 4:
        return base4(n)
    elif b == 8:
        return base8(n)
    else:
        return base16(n)

t = int(input())
while t > 0:
    b = int(input())
    n = input()
    print(solve(n, b))
    t -= 1