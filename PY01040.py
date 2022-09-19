

def devide(s):
    s1 = s[:len(s) // 2]
    s2 = s[len(s) // 2:]
    return s1, s2


def rotate(s):
    a = 0
    for i in s:
        a += (ord(i) - 65)

    ans = ''
    for i in s:
        b = ord(i) - 65 + a
        b = b % 26
        ans += chr(b + 65)
    #print(ans)
    return ans


def merge(s1, s2):
    ans = ''
    for i in range(len(s1)):
        b = (ord(s2[i]) - 65) + (ord(s1[i]) - 65)
        b = b % 26
        ans += chr(b + 65)
    print(ans)


t = int(input())
while t > 0:
    s = input()
    s1, s2 = devide(s)
    t1 = rotate(s1)
    t2 = rotate(s2)
    merge(t1, t2)
    t -= 1