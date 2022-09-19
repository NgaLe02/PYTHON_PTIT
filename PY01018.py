
p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while(True):
    tmp = input()
    if(tmp == "0"):
        break
    else:
        k, s = [str(x) for x in tmp.split()]
        k = int(k)
        if k == 0:
            break
        else:
            r = ""
            for i in range(0, len(s)):
                tmp = p.find(s[i])
                r = r + p[(tmp + k) % 28]
            r = r[::-1]
            print(r)

