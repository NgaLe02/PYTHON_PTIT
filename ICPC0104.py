import re

t = int(input())
while t > 0:
   s = input()
   list = [int(x) for x in re.findall(r'\d+', s)]
   list.sort()
   print(list[0])
   t -= 1