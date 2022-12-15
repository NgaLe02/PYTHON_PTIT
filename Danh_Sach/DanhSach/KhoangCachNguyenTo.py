MAX = 10000

def sieve(prime):
    p = 2
    while p * p <= MAX:
        if prime[p]:
            for i in range(p ** 2, MAX + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False

prime = [True for i in range(MAX + 1)]
sieve(prime)

n, x = map(int, input().split())
a = []
for i in range(len(prime)):
    if prime[i]:
        a.append(i)
        if len(a) == n + 1:
            break
    
dem = 0
while dem <= n:
    print(x, end = ' ')
    x = x + a[dem]
    dem += 1

