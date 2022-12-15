n = int(input())

dic = {}
tmp = input()
dic[tmp] = 0


dem = 1
while True:
    s = input()
    dem += 1
    if s == "":
        s = input()
        dem += 1
        dic[s] = 0
        tmp = s
    else:
        dic[tmp] += 1
    if dem == n:
        break

for key, value in dic.items():
    print(f"{key}: {value}")

