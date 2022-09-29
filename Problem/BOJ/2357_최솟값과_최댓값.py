# 2357 최솟값과 최댓값
# 220929

'''
시작시간 16:08
종료시간 16:13
'''

import sys
input = sys.stdin.readline


# 최솟값 구하는 트리
def initMin(node, s, d):
    if s == d:
        minTree[node] = nodeArr[s]
        return minTree[node]

    mid = (s+d)//2
    minTree[node] = min(initMin(node*2, s, mid), initMin((node*2) + 1, mid+1, d))
    return minTree[node]

# 최댓값 구하는 트리
def initMax(node, s, d):
    if s == d:
        maxTree[node] = nodeArr[s]
        return maxTree[node]

    mid = (s+d)//2
    maxTree[node] = max(initMax(node*2, s, mid), initMax((node*2) + 1, mid+1, d))
    return maxTree[node]

# 구간의 최솟값 구하기
def minFind(node, s, d, l, r):
    if l > d or r < s:
        return float('INF')
    
    if l <= s and d <= r:
        return minTree[node]

    mid = (s+d)//2
    return min(minFind(2*node, s, mid, l, r), minFind((2*node)+1, mid+1, d, l, r))

# 구간의 최댓값 구하기
def maxFind(node, s, d, l, r):
    if l > d or r < s:
        return -1
    
    if l <= s and d <= r:
        return maxTree[node]

    mid = (s+d)//2
    return max(maxFind(2*node, s, mid, l, r), maxFind((2*node)+1, mid+1, d, l, r))

N, M = list(map(int, input().split()))
nodeArr = [0] * (N+1)
for i in range(1, N+1):
    nodeArr[i] = int(input())

minTree = [0] * (4 * N)
maxTree = [0] * (4 * N)

initMin(1, 1, N)
initMax(1, 1, N)

for _ in range(M):
    a, b = list(map(int, input().split()))
    print(minFind(1, 1, N, a, b), end=' ')
    print(maxFind(1, 1, N, a, b))