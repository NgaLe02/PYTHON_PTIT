
bangGia = {
    ('Xe_con', '5'): 10000,
    ('Xe_con', '7'): 15000,
    ('Xe_tai', '2'): 20000,
    ('Xe_khach', '29'): 50000,
    ('Xe_khach', '45'): 70000,
}

n = int(input())
d = {}
for i in range(n):
    bienSo, loaiXe, soGheNgoi, huongDiChuyen, ngayDiChuyen  = map(str, input().split())
    if huongDiChuyen == 'IN':
        for key, val in bangGia.items():
            if loaiXe == key[0] and soGheNgoi == key[1]:
                donGia = val
        if ngayDiChuyen in d:
            d[ngayDiChuyen] += donGia
        else:
            d[ngayDiChuyen] = donGia

for key, val in d.items():
    print(f"{key}: {val}")
