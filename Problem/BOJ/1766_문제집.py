# 1766 문제집
# 221008

'''
시작시각 22:15
종료시각
'''

import heapq

N, M = list(map(int, input().split()))
arr = [0] * (N+1)
arrOrd = [[] for _ in range(N+1)]

for _ in range(M):
    node1, node2 = list(map(int, input().split()))
    arrOrd[node1].append(node2)
    arr[node2] += 1

arr[0] = float('INF')
queue = list()

for idx in range(1, N+1):
    if arr[idx] == 0:
        heapq.heappush(queue, idx)

answer = list()
while queue:
    num = heapq.heappop(queue)
    answer.append(num)
    for num2 in arrOrd[num]:
        arr[num2] -= 1
        if arr[num2] == 0:
            heapq.heappush(queue, num2)

print(*answer)