from collections import OrderedDict

s = input()

if len(s) % 2 == 1:
    s = s[:len(s) - 1]
dic = {}
for i in range(0, len(s) - 1, 2):
    x = int(s[i:i + 2])
    if not(x in dic):
        dic[x] = 1
    else:
        dic[x] = dic[x] + 1

dic1 = OrderedDict(sorted(dic.items()))
k = int(input())
check = 0
for key, value in dic1.items():
    if value >= k:
     print(f"{key} {value}")
     check = 1
if check == 0:
    print('NOT FOUND')

