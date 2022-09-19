def check(s1, s2):
    if len(s1) != len(s2):
        return 0
    for i in range (0, len(s1)):
        if s2.count(s1[i]) != s1.count(s1[i]):
            return 0
    return 1

t = int(input())
dem = 1
while dem <= t:
    s1 = input()
    s2 = input()
    print("Test " + str(dem) + ": ", end = "")
    if check(s1, s2) == 1:
        print("YES")
    else:
        print("NO")
    dem += 1