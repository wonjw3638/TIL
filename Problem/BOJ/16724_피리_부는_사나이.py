# 16724 피리 부는 사나이
# 220930

'''
시작시간 15:20
종료시간 15:40
'''

import sys
input = sys.stdin.readline
from collections import deque

N, M = list(map(int, input().split()))

arr = [list(input()) for _ in range(N)]
arrC = [[0] * M for _ in range(N)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
dp = ['U', 'L', 'D', 'R']
dn = ['D', 'R', 'U', 'L']

cnt = 0
for i in range(N):
    for j in range(M):
        if arrC[i][j] == 0:
            cnt += 1
            pi, pj = i, j
            queue = deque()
            queue.append([pi, pj])
            arrC[pi][pj] = cnt
            while queue:
                pi, pj = queue.popleft()

                for d in range(4):
                    ni = pi + di[d]
                    nj = pj + dj[d]

                    if (0 <= ni < N) and (0 <= nj < M):
                        # 내 방향으로 오는 거 or 내가 가는 거
                        if arrC[ni][nj] == 0 and (arr[ni][nj] == dp[d] or arr[pi][pj] == dn[d]):
                            arrC[ni][nj] = cnt
                            queue.append([ni, nj])

print(cnt)