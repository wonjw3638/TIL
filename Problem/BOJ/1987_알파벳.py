# 1987 알파벳
# 220929

'''
시작시각 01:06
종료시각 01:42
'''

import sys
input = sys.stdin.readline

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

# 위치, 지나온 문자열, 카운트 
def dfs(i, j, cnt):
    global answer

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if (0 <= ni < R) and (0 <= nj < C):
            alpIdx = alp.get(arr[ni][nj])
            if not visited[alpIdx]:
                visited[alpIdx] = 1
                dfs(ni, nj, cnt+1)
                visited[alpIdx] = 0


    if cnt > answer:
        answer = cnt

    return 

R, C = list(map(int, input().split()))
arr = [list(input()) for _ in range(R)]
answer = 0
alp = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7,
    'I' : 8,
    'J' : 9,
    'K' : 10,
    'L' : 11,
    'M' : 12,
    'N' : 13,
    'O' : 14,
    'P' : 15,
    'Q' : 16,
    'R' : 17,
    'S' : 18,
    'T' : 19,
    'U' : 20,
    'V' : 21,
    'W' : 22,
    'X' : 23,
    'Y' : 24,
    'Z' : 25,
}

visited = [0] * 26
visited[alp.get(arr[0][0])] = 1

dfs(0, 0, 1)
print(answer)