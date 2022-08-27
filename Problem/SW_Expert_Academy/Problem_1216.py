# 1954 달팽이 숫자
# 220821
'''
시작 12:42
끝
'''

import sys
sys.stdin = open('input.txt','r')

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    i = j = 0
    n = 1

    arr[i][j] = n

    if N != 1:
        while n <= N**2:
            for k in range(4):
                while (0 <= i + di[k] < N) and (0 <= j + dj[k] < N):
                    i += di[k]
                    j += dj[k]
                    if arr[i][j] != 0:
                        i -= di[k]
                        j -= dj[k]
                        if n == N**2:
                            n += 1
                        break
                    n += 1
                    arr[i][j] = n

    print('#{}'.format(tc))
    for ar in arr:
        print(*ar)