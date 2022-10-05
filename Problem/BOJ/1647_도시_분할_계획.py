# 1647 도시 분할 계획
# 220930

'''
시작시간 15:47
종료시간 16:08
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        tree[y] = x
    else:
        tree[x] = y

    return

def find(x):
    if x != tree[x]:
        tree[x] = find(tree[x])
    return tree[x]

N, M = list(map(int, input().split()))
arr = [tuple(map(int, input().split())) for _ in range(M)]

arr.sort(key=lambda x : x[2])

tree = [0] + [i for i in range(1, N+1)]
answer = 0
tmp = 0 
cnt = 0

for edge in arr:
    node1, node2, w = edge
    # 부모노드가 같은 경우
    if find(node1) != find(node2):
        answer += w
        cnt += 1
        union(node1, node2)

    if cnt == N-2:
        break

print(answer)