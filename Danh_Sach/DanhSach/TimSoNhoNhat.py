import re

t = int(input())

while t > 0:
    s = input()
    l = list(int(x) for x in re.findall('[0-9]+', s))
    l.sort()
    print(l[0])
    t -= 1