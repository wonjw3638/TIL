# 1149 RGM거리
# 220923

'''
설계시간 17:07 ~ 17:10
구현시간 17:11 ~ 17:19
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N)]

for idx in range(N):
    arr[idx] = list(map(int, input().split()))

minArr = [[0]*3 for _ in range(N)]

# n번째 집까지 칠하는 데 최소값
minArr[0] = arr[0]

RGB = {
    0 : [1, 2],
    1 : [0, 2],
    2 : [0, 1],
}

for i in range(1, N):
    for j in range(3):
        idx1, idx2 = RGB.get(j)
        minArr[i][j] = min(minArr[i-1][idx1] + arr[i][j], minArr[i-1][idx2] + arr[i][j])

answer = min(minArr[N-1])
print(answer)