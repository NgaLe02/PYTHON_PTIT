a, k, n = [int(x) for x in input().split()]
dem = 0
start = (a // k + 1) * k

for i in range (start, n + 1, k):
    print(i - a, end = ' ')
    dem += 1
if dem == 0:
    print("-1", end = '')
print()
