
from itertools import permutations

s = input()

s = permutations(s)

for i in s:
    print(*i, sep = '')

