
def skg(s):
    for i in range (0, len(s) - 1):
        if int(s[i]) > int(s[i + 1]):
            return 0
    return 1

t = int(input())
while t > 0:
    s = input()
    if(skg(s) == 1):
        print("YES")
    else:
        print("NO")
    t -= 1