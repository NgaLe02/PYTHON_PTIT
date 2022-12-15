import re

n = int(input())
a = []
while n > 0:
    s = input()
    for x in re.findall('[0-9]+', s):
        a.append(int(x))
    n -= 1
a.sort()
print(*a, sep = '\n')
