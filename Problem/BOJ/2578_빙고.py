player = [list(map(int, input().split())) for _ in range(5)]
answers = [list(map(int, input().split())) for _ in range(5)]
bingo = [[0] * 5 for _ in range(5)]

def BINGO():
    cnt = 0
    for answer in answers:
        for ans in answer:
            # 이중포문 탈출용
            bng = False
            for i in range(5):
                if bng == True:
                    break
                for j in range(5):
                    if player[i][j] == ans:
                        cnt += 1
                        bingo[i][j] = 1
                        bng = True
                        break
            tmp1 = tmp2 = bingo_cnt = 0
            for i in range(5):
                # 행의 합
                if sum(bingo[i]) == 5:
                    bingo_cnt += 1
                tmp = 0
                # 열의 합
                for j in range(5):
                    tmp += bingo[j][i]
                if tmp == 5:
                    bingo_cnt += 1
                tmp1 += bingo[i][i]
                tmp2 += bingo[i][4-i]
            if tmp1 == 5 or tmp2 == 5:
                bingo_cnt += 1

            if bingo_cnt >= 3:
                return cnt
            
count = BINGO()
print(count)


