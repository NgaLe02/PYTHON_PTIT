def solve(s):
    for i in s:
       if i != "4" and i != "7":
           return 0
    return 1

t = int(input())
while t > 0:
    s = input()
    if solve(s) == 0:
        print("NO")
    else:
        print("YES")
    t -= 1

