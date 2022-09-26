# 2623 음악프로그램
# 220924

import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
singers = list()
tree = [[] for _ in range(N+1)]
edge = [0] * (N+1)

for _ in range(M):
    numList = list(map(int, input().split()))
    nums = numList[0]
    
    for idx in range(1, nums):
        tree[numList[idx]].append(numList[idx+1])
        edge[numList[idx+1]] += 1

edge[0] = -1
visited = [0] * (N+1)

queue = deque()
if 0 in edge:
    startIdx = edge.index(0)
else:
    startIdx = 0

queue.append(startIdx)
visited[startIdx] = 1

while queue:
    node = queue.popleft()
    singers.append(node)
    for w in tree[node]:
        edge[w] -= 1
    for idx in range(N+1):
        if visited[idx] == 0 and edge[idx] == 0:
            queue.append(idx)
            visited[idx] = 1

if len(singers) == N:
    for singer in singers:
        print(singer)
else:
    print(0)