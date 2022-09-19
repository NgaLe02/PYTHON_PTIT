def solve(s):
    dem = 0
    s = s + " "
    for i in range (0, len(s) - 1):
        if(s[i] != s[i + 1]):
            print(str(dem + 1) + s[i], end = '')
            dem = 0
        else:
            dem += 1
    print()

t = int(input())
while t > 0:
    s = input()
    solve(s)
    t -= 1