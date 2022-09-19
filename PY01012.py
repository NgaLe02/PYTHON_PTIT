s1 = input()
s2 = input()
n = int(input())
n -= 1

for i in range (0, n):
    print(s1[i], end = '')
print(s2, end = '')
for i in range (n, len(s1)):
    print(s1[i], end = '')