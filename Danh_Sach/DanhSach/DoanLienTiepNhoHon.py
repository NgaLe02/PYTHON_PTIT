
t = int(input())
while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    stack = []
    ans = [0] * n
    for i in range(n):
        while len(stack) > 0 and a[stack[-1]] <= a[i]:
            stack.pop()
        if len(stack) == 0:
            ans[i] = i + 1
        else:
            ans[i] = i - stack[-1]
        stack.append(i)
    print(*ans)
    t -= 1