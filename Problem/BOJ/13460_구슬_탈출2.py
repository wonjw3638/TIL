# 13460 구슬 탈출2
# 220930

'''
시작시간 17:30
종료시간 
'''
from collections import deque
import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs(queue):
    redhole = False
    bluehole = False

    while queue:
        cnt, red, blue, arr = queue.popleft()
        cnt += 1
        if cnt == 11:
            return -1

        for d in range(4):
            nArr = [arr[i][:] for i in range(N)]
            ri, rj = red
            bi, bj = blue
            redMove = True
            blueMove = True

            while redMove or blueMove:
                print('####')
                print(nArr)
                nri = ri + di[d]
                nrj = rj + dj[d]
                nbi = bi + di[d]
                nbj = bj + dj[d]
                if (0 <= nri < N) and (0 <= nrj < M):
                    #  이동하려는 곳이 점인 경우
                    if nArr[nri][nrj] == '.':
                        nArr[ri][rj] = '.'
                        nArr[nri][nrj] = 'R'
                    #  이동하려는 곳이 홀인 경우
                    if nArr[nri][nrj] == 'O':
                        redMove = False
                        redhole = True
                    #  이동하려는 곳이 벽인 경우
                    if nArr[nri][nrj] == '#' or nArr[nri][nrj] == 'B':
                        redMove = False
                if (0 <= nbi < N) and (0 <= nbj < M):
                    #  이동하려는 곳이 점인 경우
                    if nArr[nbi][nbj] == '.':
                        nArr[ri][rj] = '.'
                        nArr[nbi][nbj] = 'R'
                    #  이동하려는 곳이 홀인 경우
                    if nArr[nbi][nbj] == 'O':
                        blueMove = False
                        bluehole = True
                    #  이동하려는 곳이 벽인 경우
                    if nArr[nbi][nbj] == '#' or nArr[nbi][nbj] == 'R':
                        blueMove = False

                # 빨간공이 먼저 골인
                if redhole == True:
                    if bluehole == False:
                        return cnt
                    # 둘다 골인
                    else:
                        return -1
                # 파란공이 먼저 골인
                if bluehole == True and redhole == False:
                    return -1
            
            queue.append((cnt, (ri, rj), (bi, bj), nArr))

N, M = list(map(int, input().split()))
arr = list()

for i in range(N):
    arrInput = list(input())
    arr.append(arrInput)
    for j in range(M):
        if arrInput[j] == 'R':
            red = [i, j]
        if arrInput[j] == 'B':
            blue = [i, j]

queue = deque()
queue.append((0, red, blue, arr))
answer = bfs(queue)

print(bfs)