
t = int(input())
l = []
while t > 0:
    s = input()
    l.append(s)
    t -= 1
l = set(l)
print(len(l))