t = int(input())
while t > 0:
    s = input()
    s = str(sorted(s))
    tong = 0
    for i in range(0, len(s)):
        if s[i].isdigit() == True:
            tong += int(s[i])
    for i in range (0, len(s)):
        if s[i].isalpha() == True:
          print(s[i], end = '')
    print(tong)
    t -= 1