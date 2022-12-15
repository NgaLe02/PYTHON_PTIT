
t = int(input())
while t > 0:
    a = [str(x) for x in input().split()]
    ans = ''
    for i in a:
        if len(ans) + len(i) <= 100:
            ans += i + " "
        else:
            break
    print(ans)
    t -= 1