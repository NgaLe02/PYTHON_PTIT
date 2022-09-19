def check(s1):
    s2 = s1[::-1]
    for i in range (1, len(s1)):
        if(abs(ord(s1[i]) -ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1]))):
            return 0
    return 1

t = int(input())
while t > 0:
    s1 = input()
    if(check(s1) == 1):
        print("YES")
    else:
        print("NO")
    t -= 1