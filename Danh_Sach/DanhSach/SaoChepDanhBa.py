def xulyten(s):
    a = list(s.split())[::-1]
    return "".join(a)


with open(r"SOTAY.txt", "r") as f:
    data = f.readlines()
    a = []
    date = ""
    s = []
    for line in data:
        # xoa khoang trang 2 dau va \n
        line = line.strip()
        if line[:4] == "Ngay":
            # in ra doan 15/11/2021
            date = line[5:]
        # neu khac ngay va khong phai la so
        elif not line.isdigit():
            # push chuoi chi co chu vao s
            s.append(line)  # Nguyen Van A
        # toan so
        else:
            s.append(line+" "+date)  # Nguyen Van A: 0000000 15/11/2021
            a.append(s)
            s = []  # khoi tao s bang rong
    a.sort(key=lambda x: (xulyten(x[0])))

with open("DIENTHOAI.txt", "w") as file:
    for x in a:
        file.write(x[0]+": "+x[1]+"\n")