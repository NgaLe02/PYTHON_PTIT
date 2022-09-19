def check(s):
    if len(s) % 2 == 0:
        return 0
    if s[0] == s[1]:
        return 0
    for i in range (0, len(s) - 2, 2):
        if s[i] != s[i + 2]:
            return 0
    return 1

t = int(input())
while t > 0:
    s = input()
    if check(s) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1