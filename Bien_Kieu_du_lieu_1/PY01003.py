t = int(input())
while t > 0:
    s = (input())
    if len(s) < 2:
        print(s)
    else:
        l = len(s)
        mem = 0
        for i in range(l - 1, 0, -1):
           # print("Gia tri cua s[i] = " + s[i])
            tmp = int(s[i]) + mem
           # print("tmp = " + str(tmp))
            if tmp >= 5:
                mem = 1
            else:
                mem = 0

        tmp = int(s[0]) + mem
       # print("tmp = " + str(mem))
        print(tmp, end = '')
       # print("Do dai cua xau: " + str(l))
        for i in range (l - 1):
           print("0", end = ''),
    print()
    t = t - 1
