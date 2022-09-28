# 17142 연구소3
# 220928

import sys
input = sys.stdin.readline
from collections import deque

def comb(arr, n):
    result = list()

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for j in comb(arr[i + 1:], n - 1):
            result.append([elem] + j)

    return result

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs(arr):
    global answer
    cnt = 0
    active = list()

    while queue:
        i, j = queue.popleft()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if (0 <= ni < N) and (0 <= nj < N):
                if arr[ni][nj] == '0':
                    arr[ni][nj] = arr[i][j] + 1
                    queue.append((ni, nj))
                elif arr[ni][nj] == '*':
                    active.append((ni, nj))
                    arr[ni][nj] = arr[i][j] + 1
                    queue.append((ni, nj))
    
    for i in range(N):
        for j in range(N):
            # 바이러스가 없는 칸이 있는 경우
            if arr[i][j] == '0':
                if answer == float('INF'):
                    answer = -1
                return
            if arr[i][j] == '1' or arr[i][j] == '*': continue
            # 바이러스 놓는데 걸리는 시간
            if arr[i][j] > cnt :
                if (i, j) in active:
                    continue
                cnt = arr[i][j]
    # 최소시간 update
    if answer == -1:
        answer = cnt
    if answer > cnt:
        answer = cnt

    return

N, M = list(map(int, input().split()))
arr = list()
virus = list()

for i in range(N):
    # 바이러스 개수와 구분하기 위해서 벽은 문자열로 저장
    arrInput = list(input().split())
    # 바이러스 위치 따로 저장
    for j in range(N):
        if arrInput[j] == '2':
            virus.append([i, j])
            # 비활성 바이러스로 표시
            arrInput[j] = '*'
    arr.append(arrInput)

answer = float('INF')
virusComb = comb(virus, M)

for virusList in virusComb:
    queue = deque()
    arrTmp = [arr[i][:] for i in range(N)]
    for i, j in virusList:
        arrTmp[i][j] = 0
        queue.append((i, j))
    
    bfs(arrTmp)
    if answer == 0:
        break

print(answer)