# 11724 연결요소의 개수
# 221203

'''
시작시각 03:01
종료시각 03:17
'''

# 정점 개수 N, 간선 개수 M
N, M = map(int, input().split())

# 그래프 상황을 기록할 list
arr = [[] for _ in range(N + 1)]
# 연결 요소를 체크할 list
visit = [0] * (N + 1)

# 연결 요소의 개수를 셀 변수
answer = 0

# 그래프 입력값 받아서 정리
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

# dfs 함수
def dfs(n):
    # 방문한 정점인 경우 끝!
    if visit[n] == 1:
        return 
    
    # 방문했던 정점이 아닌 경우 -> 방문 표시, 연결된 정점 확인
    visit[n] = 1
    for nexU in arr[n]:
        dfs(nexU)

for chk in range(1, N+1):
    if visit[chk] == 0:
        answer += 1
        dfs(chk)

print(answer)