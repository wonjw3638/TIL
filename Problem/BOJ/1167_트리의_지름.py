# 1167 트리의 지름
# 220923

'''
시작시각 00:28
종료시각:
'''

import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]

# def dfs(s):
#     global ans
#     global farNode

#     visited = [0] * (N + 1)
#     stack = [0] * (N + 1)
#     top = -1
#     v = s
    
#     top += 1
#     stack[top] = v
#     visited[v] = 1

#     while top >= 0:
#         v = stack[top]
#         for i, w in  tree[v]:
#             if visited[i] == 0:
#                 visited[i] = visited[v] + w
#                 if visited[i] > ans:
#                     ans = visited[i]
#                     farNode = i
#                 top += 1
#                 stack[top] = i
#                 break
#         else:
#             top -= 1

#     return ans-1, farNode

def dfs(node, weight):
    global answer
    global farNode
    
    visited[node] = 1
    
    if weight > answer:
        answer = weight
        farNode = node

    for i, w in tree[node]:
        if visited[i] == 0:
            nextWeight = weight + w
            dfs(i, nextWeight)

for _ in range(N):
    inputArr = list(map(int, input().split()))
    idx = 1
    while True:
        if inputArr[idx] == -1:
            break
        else:
            tree[inputArr[0]].append([inputArr[idx], inputArr[idx+1]])
            idx += 2

farNode = answer = 0

visited = [0] * (N+1)
dfs(1, 0)

visited = [0] * (N+1)
dfs(farNode, 0)

print(answer)