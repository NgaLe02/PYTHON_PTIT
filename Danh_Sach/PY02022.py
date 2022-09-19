import math


def snt(n):
    if n < 2:
        return 0
    for i in range (2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1


n = int(input())

list = [int(x) for x in input().split()]

list_new = sorted(set(list), key = list.index)

for i in list_new:
    if snt(i):
      x = list.count(i)
      print(f"{i} {x}")