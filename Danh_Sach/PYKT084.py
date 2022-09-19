n = int(input())

dic = {}
tmp = input()
dic[tmp] = 0
#mem = 1: input() truoc do la cau chu de
#mem = 0: input() truoc do la xau rong, bay h se la cau chu de
mem = 1

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

