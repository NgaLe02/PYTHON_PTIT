

def sumTripleZero (n, l):
    ans = 0
    for i in range(0, n - 2):
        j = i + 1
        k = n - 1
        while j < k:
            if l[i] + l[k] + l[j] == 0:
              ans += 1
              j += 1
            elif l[i] + l[k] + l[j] < 0:
              j += 1
            else:
              k -= 1
    return ans


t = int(input())

while t > 0:
    n = int(input())
    l = list(int(x) for x in input().split())
    l.sort()
    print(sumTripleZero(n , l))
    t -= 1