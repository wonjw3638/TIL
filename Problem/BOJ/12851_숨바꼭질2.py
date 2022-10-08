# 12851 숨바꼭질2
# 221005

from collections import deque

N, K = list(map(int, input().split()))

def bfs():
    visited = [0] *  200000
    visited[N] = 1

    queue = deque()
    queue.append((N, 0))
    answer = float('INF')
    count = 0

    while queue:
        num, cnt = queue.popleft()
        print(num, cnt)
        if num == K or answer != float('INF'):
            if answer == float('INF'):
                answer = cnt
            if answer == cnt:
                count += 1
            continue
        
        cnt += 1
        for d in [1, -1, num]:

            if 0 <= num+d < 200000 and visited[num + d] == 0:
                visited[num + d] = 1
                queue.append((num+d, cnt))
    
    return answer, count

answer, count = bfs()
print(answer)
print(count)
