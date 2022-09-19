s1 = input()
s2 = input()

s1 = s1.lower()
s2 = s2.lower()

words1 = s1.split()
words2 = s2.split()
words1 = set(words1)
words2 = set(words2)

hop = words1.union(words2)
giao = words1.intersection(words2)
hop = sorted(hop)
giao = sorted(giao)
for x in hop:
    print(x, end = ' ')
print()
for x in giao:
    print(x, end=' ')