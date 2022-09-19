
t = int(input())
while t > 0:
    d, m = [int(x) for x in input().split()]
    if (m == 3 and d >= 21) or (m == 4 and d <= 19):
        print('Bach Duong')
    elif (m == 4 and d >= 20) or(m == 5 and d <= 20):
        print('Kim Nguu')
    elif (m == 5 and d >= 21) or(m == 6 and d <= 20):
        print('Song Tu')
    elif (m == 6 and d >= 21) or(m == 7 and d <= 22):
        print('Cu Giai')
    elif (m == 7 and d >= 23) or(m == 8 and d <= 22):
        print('Su Tu')
    elif (m == 8 and d >= 23) or(m == 9 and d <= 22):
        print('Xu Nu')
    elif (m == 9 and d >= 23) or(m == 10 and d <= 22):
        print('Thien Binh')
    elif (m == 10 and d >= 23) or (m == 11 and d <= 22):
        print('Thien Yet')
    elif (m == 11 and d >= 23) or(m == 12 and d <= 21):
        print('Nhan Ma')
    elif (m == 12 and d >= 22) or(m == 1 and d <= 19):
        print('Ma Ket')
    elif (m == 1 and d >= 20) or(m == 2 and d <= 18):
        print('Bao Binh')
    elif (m == 2 and d >= 19) or(m == 3 and d <= 20):
        print('Song Ngu')
    t -= 1

    # t = int(input())
    # data = {((21, 3), (19, 4)): "Bach Duong", ((20, 4), (20, 5)): "Kim Nguu",
    #         ((21, 5), (20, 6)): "Song Tu", ((21, 6), (22, 7)): "Cu Giai",
    #         ((23, 7), (22, 8)): "Su Tu", ((23, 8), (22, 9)): "Xu Nu",
    #         ((23, 9), (22, 10)): "Thien Binh", ((23, 10), (22, 11)): "Thien Yet",
    #         ((23, 11), (21, 12)): "Nhan Ma", ((22, 12), (19, 1)): "Ma Ket",
    #         ((20, 1), (18, 2)): "Bao Binh", ((19, 2), (20, 3)): "Song Ngu"}
    # while t > 0:
    #     d, m = [int(x) for x in input().split()]
    #     for x in data.keys():
    #         if (m == x[0][1] and d >= x[0][0]) or (m == x[1][1] and d <= x[1][0]):
    #             print(data[x])
    #             break
    #     t = t - 1