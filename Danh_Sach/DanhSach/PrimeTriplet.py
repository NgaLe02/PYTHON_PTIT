
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
prime = [True for i in range(MAX + 1)]
sieve(prime)

while t > 0:
    n = int(input())
    count = 0
    for i in range (5, n - 5):
        if prime[i] and prime[i + 2] and prime[i + 6]:
            count += 1
        if prime[i] and prime[i + 4] and prime[i + 6]:
            count += 1
    print(count)
    t -= 1