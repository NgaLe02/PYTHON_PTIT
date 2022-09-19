import math

MAX = 1000000

def sieve(prime):
    p = 2
    while p * p <= MAX:
        if prime[p]:
            for i in range(p ** 2, MAX + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False


n, x = [int(x) for x in input().split()]

prime = [True for i in range (MAX + 1)]
mem = 0
print(x, end=' ')
sieve(prime)

while n > 0:
    if prime[mem]:
        print(x + mem, end=' ')
        x = x + mem
        n -= 1
    mem += 1