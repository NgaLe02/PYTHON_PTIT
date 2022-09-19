
t = int(input())

while t > 0:
    s = input()
    if s[0] == s[len(s) - 1]:
        print("YES")
    else:
        print("NO")
    t -= 1