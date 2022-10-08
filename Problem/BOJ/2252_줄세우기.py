# 2252 줄 세우기
# 220930

'''
시작시간 10:27
종료시간 10:35
'''

import sys
input = sys.stdin.readline
from collections import deque

N, M = list(map(int, input().split()))

# idx학생 다음에 와야하는 학생
edge = [[] for _ in range(N+1)]
# idx학생 앞에 와야하는 학생 수
tree = [-1] + [0] * (N)

for _ in range(M):
    stu1, stu2 = list(map(int, input().split()))
    edge[stu1].append(stu2)
    tree[stu2] += 1

queue = deque()

for idx, stu in enumerate(tree):
    if stu == 0:
        queue.append(idx)
        # 방문 표시
        tree[idx] = -1

answer = list()

while queue:
    stu = queue.popleft()
    answer.append(stu)

    nexStu = edge[stu]
    for nex in nexStu:
        tree[nex] -= 1
    
    for idx, stu in enumerate(tree):
        if stu == 0:
            queue.append(idx)
            # 방문 표시
            tree[idx] = -1

print(*answer)