
def isIPAddress(x):
    if len(x) != 4:
        return False
    for i in x:
        if i.isdecimal():
            if int(i) < 0 or int(i) > 255:
                return False
        else:
            return False
    return True


t = int(input())

while t > 0:
    if isIPAddress(input().split('.')):
        print('YES')
    else:
        print('NO')
    t -= 1