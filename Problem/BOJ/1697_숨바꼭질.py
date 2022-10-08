# 1697 숨바꼭질
# 221004

from collections import deque

N, K = list(map(int, input().split()))

def bfs():
    visited = [0] *  200000
    visited[N] = 1

    queue = deque()
    queue.append((N, 0))

    while queue:
        num, cnt = queue.popleft()
        if num == K:
            return cnt
        
        cnt += 1
        for d in [1, -1, num]:

            if 0 <= num+d < 200000 and visited[num + d] == 0:
                visited[num + d] = 1
                queue.append((num+d, cnt))
    return 

answer = bfs()
print(answer)
