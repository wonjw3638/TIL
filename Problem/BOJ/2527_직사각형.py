for _ in range(4):
    rec = list(map(int, input().split()))
    rec1 = rec[:4]
    rec2 = rec[4:]

    if (rec1[2] < rec2[0]) or (rec2[2] < rec1[0]) or (rec1[3] < rec2[1]) or (rec1[1] > rec2[3]):
        print('d')
    elif (rec1[0] == rec2[2]) or (rec1[2] == rec2[0]) :
        if (rec1[1] == rec2[3]) or  (rec1[3] == rec2[1]):
            print('c')
        else:
            print('b')
    elif (rec1[1] == rec2[3]) or  (rec1[3] == rec2[1]):
        print('b')
    else:
        print('a')