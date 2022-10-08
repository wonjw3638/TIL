# 17404 RGB 거리2
# 220930

'''
시작시간 09:12
종료시간 10:24
'''

import sys
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N)]

for idx in range(N):
    arr[idx] = list(map(int, input().split()))

maxTmp = float('INF')

RminArr = [[maxTmp]*3 for _ in range(N)]
GminArr = [[maxTmp]*3 for _ in range(N)]
BminArr = [[maxTmp]*3 for _ in range(N)]

# n번째 집까지 칠하는 데 최소값
RminArr[0] = [arr[0][0], maxTmp, maxTmp] 
GminArr[0] = [maxTmp, arr[0][1], maxTmp] 
BminArr[0] = [maxTmp, maxTmp, arr[0][2]] 

RGB = {
    0 : [1, 2],
    1 : [0, 2],
    2 : [0, 1],
}

for i in range(1, N-1):
    for j in range(3):
        idx1, idx2 = RGB.get(j)
        RminArr[i][j] = min(RminArr[i-1][idx1] + arr[i][j], RminArr[i-1][idx2] + arr[i][j])
    for j in range(3):
        idx1, idx2 = RGB.get(j)
        GminArr[i][j] = min(GminArr[i-1][idx1] + arr[i][j], GminArr[i-1][idx2] + arr[i][j])
    for j in range(3):
        idx1, idx2 = RGB.get(j)
        BminArr[i][j] = min(BminArr[i-1][idx1] + arr[i][j], BminArr[i-1][idx2] + arr[i][j])

# N-1일때는 따로 해줌
# 첫번째에 빨간색, 마지막에 초록/파랑
RminArr[N-1][1] = min(RminArr[N-2][0] + arr[N-1][1], RminArr[N-2][2] + arr[N-1][1])
RminArr[N-1][2] = min(RminArr[N-2][0] + arr[N-1][2], RminArr[N-2][1] + arr[N-1][2])

# 첫번째에 초록색, 마지막에 빨강/파랑
GminArr[N-1][0] = min(GminArr[N-2][1] + arr[N-1][0], GminArr[N-2][2] + arr[N-1][0])
GminArr[N-1][2] = min(GminArr[N-2][0] + arr[N-1][2], GminArr[N-2][1] + arr[N-1][2])

# 첫번째에 파랑색, 마지막에 빨강/초록
BminArr[N-1][0] = min(BminArr[N-2][1] + arr[N-1][0], BminArr[N-2][2] + arr[N-1][0])
BminArr[N-1][1] = min(BminArr[N-2][0] + arr[N-1][1], BminArr[N-2][2] + arr[N-1][1])

answer = min(min(RminArr[N-1]), min(GminArr[N-1]), min(BminArr[N-1]))

print(answer)