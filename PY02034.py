s = input()

if len(s) % 2 == 1:
    s = s[0:-1]
d = {}

for i in range (0, len(s), 2):
    x = int(s[i:i + 2])
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
for key, value in d.items():
    print(f"{key} {value}")
