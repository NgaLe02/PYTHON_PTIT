s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def solve(n, b  ):
    tmp = "";
    while n > 0:
        tmp = s[n % b] + tmp
        n = n // b
    return tmp;

t = int(input())
while t > 0:
    n, b = [int(x) for x in input().split()]
    print(solve(n, b))
    t -= 1