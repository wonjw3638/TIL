# 2042 구간 합 구하기
# 220929

'''
시작시간 13:34
종료시간 15:00
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 세그먼트 트리 생성 함수
# node 번호, 보고 있는 노드의 범위 start, end
def init(node, s, d):
    
    if s == d:
        tree[node] = nodeList[s]
        return nodeList[s]
    
    mid = (s+d)//2
    tree[node] = init(2*node, s, mid) + init((2*node) + 1, (mid)+1, d)
    return tree[node]

# 합 구하는 함수
# node 번호, 보고 있는 노드의 범위 start, end, 내가 더하려는 범위 left, right
def sumTree(node, s, d, l, r):
    if l > d or r < s:
        return 0

    if l <= s and r >= d:
        return tree[node]
    else:
        mid = (s+d)//2
        return sumTree(2 * node, s, mid, l, r) + sumTree((2 * node)+1, (mid)+1, d, l, r)

# update
# node번호, node 범위 s, d, 업데이트 하려는 노드번호 u, 차이값 diff
def update(node, s, d, u, diff):

    if s == d :
        tree[node] += diff
        return 
    
    if s <= u <= (s+d)//2:
        tree[node] += diff
        return update(2 * node, s, (s+d)//2, u, diff)
    else:
        tree[node] += diff
        return update((2 * node) + 1, (s+d)//2 + 1, d, u, diff)


N, M, K = list(map(int, input().split()))
nodeList = [0] + [int(input()) for _ in range(N)]

# 트리의 노드 개수 구하기
# 0은 빼고, 노드번호는 1부터~idx까지
tree = [0] * (N*4)

init(1, 1, N)

for _ in range(M+K):
    a, b, c = list(map(int, input().split()))
    if a == 1:
        diff = c - nodeList[b]
        nodeList[b] = c
        update(1, 1, N, b, diff)
    else:
        print(sumTree(1, 1, N, b, c))
