# 12100 2048(Easy)
# 220926

import sys
input = sys.stdin.readline

# 위 오른쪽 아래 왼쪽
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

moveRange = {
    0 : [range(N), range(N)],
    1 : [range(N), range(N-1, -1, -1)],
    2 : [range(N-1, -1, -1), range(N)],
    3 : [range(N), range(N)],
    }

def move(arrMove, d):
    moved = [[0]*N for _ in range(N)]

    iRange, jRange = moveRange[d]
    for i in iRange:
        for j in jRange:
            num = arrMove[i][j]
            if num :
                ni = i + di[d]
                nj = j + dj[d]
                pi, pj = i, j

                while (0 <= ni < N) and (0<= nj < N):
                    # 빈칸인 경우 -> 이동
                    if arrMove[ni][nj] == 0:
                        arrMove[pi][pj] = 0
                        arrMove[ni][nj] = num

                        pi, pj = ni, nj
                        ni = pi + di[d]
                        nj = pj + dj[d]
                    # 같은 숫자인 경우 더하기
                    elif (arrMove[ni][nj] == num) and (moved[ni][nj] == 0):
                        arrMove[pi][pj] = 0
                        arrMove[ni][nj] = 2 * num
                        # 이번에 합친 거 표시
                        moved[ni][nj] = 1
                        break
                    # 다른 숫자인 경우 이동x
                    else:
                        break

    return arrMove


def play(arrPlay, K):
    global answer

    if K == 0:
        tmp = max([max(arrPlay[i]) for i in range(N)])
        if tmp > answer:
            answer = tmp
        return 

    # 위아래오른쪽왼쪽 이동 가능
    for d in range(4):
        # 딥카피
        arrTmp = [arrPlay[i][:] for i in range(N)]
        # 이동후 결과 배열 반환
        arrMoved = move(arrTmp, d)
        play(arrMoved, K-1)

    return 

# 최대 5번 이동 가능
play(arr, 5)

print(answer)
