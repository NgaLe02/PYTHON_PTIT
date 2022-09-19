t = ""
check = 0
while True:
    try:
        s = input()
        if s != '.' and s != '?' and s != '!':
            if check == 0:
                s = s.lower()
                s = s.title()
            else:
                s = s.lower()
                check = 1
            t += " " + s
        elif s == ',' or s == ':':
            t += s
        else:
            t += '\n'
            check = 0
    except EOFError:
         break
print(t)