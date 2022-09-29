# 10868 최솟값
# 220929

'''
시작시간 15:39
종료시간 16:06
'''

import sys
input = sys.stdin.readline


# 트리를 해당 구간의 최솟값으로 채우기
def init(node, s, d):
    if s == d:
        tree[node] = nodeArr[s]
        return tree[node]

    mid = (s+d)//2
    tree[node] = min(init(node*2, s, mid), init((node*2) + 1, mid+1, d))
    return tree[node]

# 구간의 최솟값 구하기
def find(node, s, d, l, r):
    if l > d or r < s:
        return float('INF')
    
    if l <= s and d <= r:
        return tree[node]

    mid = (s+d)//2
    return min(find(2*node, s, mid, l, r), find((2*node)+1, mid+1, d, l, r))

N, M = list(map(int, input().split()))
nodeArr = [0] * (N+1)
for i in range(1, N+1):
    nodeArr[i] = int(input())

tree = [0] * (4 * N)

init(1, 1, N)

for _ in range(M):
    a, b = list(map(int, input().split()))
    print(find(1, 1, N, a, b))


