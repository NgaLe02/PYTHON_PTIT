
n = int(input())
list = []
while True:
    for x in input().split():
       list.append(int(x))
    if len(list) == n:
        break
check = [0 for i in range(30001)]
for i in list:
    check[i]  = 1
for i in range(1,n+2):
    if check[i] == 0:
     print(i)
     break