def check(s):
    tmp = s.split(".")
    if tmp[1].lower() == 'py':
        return 1
    return 0

s = input()
if check(s) == 1:
    print("yes")
else:
    print("no")