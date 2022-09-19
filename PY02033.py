
s = input()

if len(s) % 2 == 1:
    s = s[:len(s) - 1]
a = []

for i in range(0, len(s)  - 1, 2):
    x = int(s[i:i + 2])
    if not(x in a):
        a.append(x)
print(*a)

