
def solve(n):
    mul = 1
    for i in n:
        if i != '0':
           mul *= int(i)
    return mul

t = int(input())
while t > 0:
    n = input()
    print(solve(n))
    t -= 1