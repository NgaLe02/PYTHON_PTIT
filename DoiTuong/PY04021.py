import datetime


class Time:
    def __init__(self, mnc, tnc, giovao, giora):
        self.ma = mnc
        self.ten = tnc.strip()
        self.gioVao = giovao
        self.gioRa = giora
        self.thoiGian = ''

    def time_play(self):
        gioVao = datetime.datetime.strptime(self.gioVao, '%H:%M')
        gioRa = datetime.datetime.strptime(self.gioRa, '%H:%M')
        self.thoiGian = gioRa - gioVao

    def __str__(self):
        tmp = str(self.thoiGian)
        t = [int(x) for x in tmp.split(":")]
        return f"{self.ma} {self.ten} {t[0]} gio {t[1]} phut"


n = int(input())
a = []
for i in range(n):
    a.append(Time(input(), input(), input(), input()))
    a[i].time_play()

a.sort(key=lambda x: x.thoiGian, reverse=True)

for i in a:
    print(i)
