import math
def solve(n):
    print("1", end = '')
    for i in range (2, int(math.sqrt(n)) + 1):
        dem = 0
        while n % i == 0:
            dem += 1
            n /= i
        if dem != 0:
         print(" * " + str(i) + "^" + str(dem), end = '')
    if(n != 1):
        print(" * " + str(int(n)) + "^1", end = '')
    print()

t = int(input())
while t > 0:
    n = int(input())
    solve(n)
    t -= 1