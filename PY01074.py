minPrimes = []
def sieve():
    for i in range (2, 2000003):
        minPrimes.append(0)
    for i in range (2, 2000001):
        if minPrimes[i] == 0:
            for j in range(i * i, 2000001):
                if minPrimes[j] == 0:
                    minPrimes[j] = 1
    for i in range (2, 2000001):
        if minPrimes[i] == 0:
            minPrimes[i] = i

def solve(n):
    tong = 0
    while n != 1:
        tong += minPrimes[n]
        n = int(n / minPrimes[n])
    return tong

t = int(input())
tong = 0
sieve()
while t > 0:
    n = int(input())
    tong += solve(n)
    t -= 1
print(tong)