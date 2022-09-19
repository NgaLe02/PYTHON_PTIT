n = int(input())

dic = {}
for i in range (0, n):
    bienSo, loaiXe, soGheNgoi, huongDiChuyen, ngayDiChuyen = (str(x) for x in input().split())
    if huongDiChuyen == 'IN':
        if loaiXe == 'Xe_con':
            if soGheNgoi == '5':
                donGia = 10000
            else:
                donGia = 15000
        elif loaiXe == 'Xe_tai':
            donGia = 20000
        elif loaiXe == 'Xe_khach':
            if soGheNgoi == '29':
                donGia = 50000
            else:
                donGia = 70000
        if not (ngayDiChuyen in dic):
            dic[ngayDiChuyen] = donGia
        else:
            dic[ngayDiChuyen] += donGia

for key, value in dic.items():
    print(f"{key}: {value}")
