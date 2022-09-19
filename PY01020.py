def spl(s):
    tmp = s[-2:]
    if tmp == '86':
        return 1
    return 0

t = int(input())
while t > 0:
    s = input()
    if(spl(s) == 1):
        print("YES")
    else:
        print("NO")
    t -= 1