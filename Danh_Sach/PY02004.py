n = int(input())
list = input().split()
ans = 0;
for i in range (len(list) - 1):
    if list[i] != list[i + 1]:
        ans += 1
print(ans)