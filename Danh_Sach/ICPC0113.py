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


t = int(input())

while t > 0:
    n = int(input())
    prime = [True for i in range(MAX + 1)]
    sieve(prime)
    for i in range (13, n):
       if prime[i]:
           m = str(i)
           rev = int(m[::-1])
           if i != rev and rev < n and prime[rev]:
            print(f"{i} {rev} ", end = '')
            prime[rev] = False
    print()
    t -= 1