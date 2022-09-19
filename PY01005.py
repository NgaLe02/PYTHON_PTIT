def solve(s):
    dem = 0
    for i in s:
       if i == "4" or i == "7":
           dem += 1
    if dem == 4 or dem == 7:
        return 1
    return 0

s = input()
if solve(s) == 0:
    print("NO")
else:
    print("YES")
