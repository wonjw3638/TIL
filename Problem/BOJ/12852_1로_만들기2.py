# 12852 1로 만들기2
# 220930

'''
시작시간 16:45
종료시간 17:26
'''

from collections import deque

N = int(input())
visited = [0] * (N+1)

queue = deque()
queue.append([N, [N]])

while True:
    n, ans = queue.popleft()
    if n == 1:
        answer = ans
        break

    if (visited[n//3] == 0) and (n%3 == 0 and n >= 3):
        visited[n//3] = 1
        queue.append((n//3, ans + [n//3]))
    if (visited[n//2] == 0) and (n%2 == 0 and n >= 2):
        visited[n//2] = 1
        queue.append((n//2, ans + [n//2]))
    if visited[n-1] == 0:
        visited[n] = 1
        queue.append((n-1, ans + [n-1]))


print(len(answer)-1)
print(*answer)