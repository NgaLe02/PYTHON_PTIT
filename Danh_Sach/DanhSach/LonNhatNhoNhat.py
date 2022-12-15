
while True:
    n = int(input())
    if n == 0:
        break
    a = []
    for i in range(n):
        a.append(int(input()))
    ln = max(a)
    bn = min(a)
    if ln != bn:
        print(f"{bn} {ln}")
    else:
        print("BANG NHAU")