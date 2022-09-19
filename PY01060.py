def tongcs(s):
    add = 0
    for i in range (1, len(s), 2):
        add += int(s[i])
    return add

def tichcs(s):
    mul = 1
    dem = 0
    for i in range (0, len(s), 2):
        if s[i] == '0':
            dem += 1
        if s[i] != '0':
            mul *= int(s[i])
    if mul == 1 and dem == len(s) // 2:
        return 0
    return mul

t = int(input())
while t > 0:
    s = input()
    print(tichcs(s), end = ' ')
    print(tongcs(s))
    t -= 1