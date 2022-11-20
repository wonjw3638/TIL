N, M = list(map(int, input().split()))
room = [0] + list(map(int, input().split()))
areaMap = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    n1, n2, w = list(map(int, input().split()))
    areaMap[n1][n2] = w
    areaMap[n2][n1] = w

answer = -1

def dfs():
    pass

cnt = 0
dfs(1, N, cnt)