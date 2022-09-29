# 11505 구간 곱 sum구하기
# 220929

'''
시작시간 16:15
종료시간 17:52
'''

import sys
input = sys.stdin.readline
mod = 1000000007

# 세그먼트 트리 생성 함수
# node 번호, 보고 있는 노드의 범위 start, end
def init(node, s, d):
    
    if s == d:
        tree[node] = nodeList[s]
        return nodeList[s]
    
    mid = (s+d)//2
    tree[node] = (init(2*node, s, mid) * init((2*node) + 1, mid + 1, d)) % mod
    return tree[node]

# 곱 구하는 함수
# node 번호, 보고 있는 노드의 범위 start, end, 내가 더하려는 범위 left, right
def mulTree(node, s, d, l, r):
    if l > d or r < s:
        return 1

    if l <= s and r >= d:
        return tree[node]
    else:
        mid = (s+d)//2
        return (mulTree(2 * node, s, mid, l, r) * mulTree((2 * node)+1, (mid)+1, d, l, r)) % mod

def update(node, s, d):
    if b < s or d < b:
        return tree[node]
    
    if s == d:
        tree[node] = c
        return tree[node]
    
    mid = (s+d)//2
    if s <= b <= mid:
        tree[node] = (update(2*node, s, mid) * tree[(2*node)+1]) % mod
        return tree[node]
    else:
        tree[node] = (update(2*node + 1, mid+1, d) * tree[(2*node)]) % mod
        return tree[node]


N, M, K = list(map(int, input().split()))
nodeList = [0] + [int(input()) for _ in range(N)]

# 트리의 노드 개수 구하기
# 0은 빼고, 노드번호는 1부터~idx까지
i = 0
while True:
    if N < 2**i:
        i += 1
        break
    else:
        i += 1

tree = [1] * (2**i)

init(1, 1, N)

for _ in range(M+K):
    a, b, c = list(map(int, input().split()))
    if a == 1:
        update(1, 1, N)
    else:
        print(int(mulTree(1, 1, N, b, c)))