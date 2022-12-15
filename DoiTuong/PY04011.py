
def check():
    for i in a:
        b = [x for x in i.split()]
        if b[0] > b[2]:
            tmp = '<'
        else:
            tmp = '>'
        if tmp != b[1]:
            return 0
    return 1

t = int(input())
a = []
for i in range(t):
    a.append(input().strip())

if check():
    print('possible')
else:
    print('impossible')