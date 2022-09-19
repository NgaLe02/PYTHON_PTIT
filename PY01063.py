
def solve(s, tmp):
    dem = 0
    i = 0
    while i < len(s):
        if s.find(tmp, i) != -1:
            #print(s.find(tmp, i))
            dem += 1
            i = s.find(tmp, i) + len(tmp)
        else:
            break
    return dem

t = int(input())
while t > 0:
    s = input()
    tmp = input()
    #solve(s, tmp)
    print(solve(s, tmp))
    t -= 1