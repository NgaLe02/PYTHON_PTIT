import re

t = int(input())
list = []
while t > 0:
   s = input()
   list.extend(int(x) for x in re.findall(r'\d+', s))
   t -= 1

list.sort()
for i in list:
       print(i)