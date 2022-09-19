def solve(s):
    res = ''
    for i in s:
        if(i.isdigit() == True):
            print(res * int(i), end = '')
        else:
            res = i
    print()
t = int(input())
while t > 0:
    s = input()
    solve(s)
    t -= 1