# 2268 수들의 합7
# 221001

import sys
input = sys.stdin.readline

# 트리 생성
def init(node, s, d):

    if s == d:
        tree[node] = nodeArr[s]
        return tree[node]
    
    mid = (s+d)//2
    tree[node] = init(node*2, s, mid) + init(node*2 + 1, mid+1, d)
    return tree[node]

# 구간합 출력
def sumTree(node, s, d, l, r):
    if l > d or r < s:
        return 0

    if l <= s and d <= r:
        return tree[node]

    mid = (s+d)//2
    return sumTree(node*2, s, mid, l, r) + sumTree(node*2 + 1, mid+1, d, l, r) 

# 함수 업데이트
def update(node, s, d, b, diff):
    if s == d and s == b:
        tree[node] += diff
        return 

    if s <= b <= d:
        tree[node] += diff
    
    mid = (s+d)//2
    if b > mid:
        update(node*2 + 1, mid+1, d, b, diff)
    else:
        update(node*2, s, mid, b, diff)

N, M = list(map(int, input().split()))

# 트리 노드 개수는 N보다 큰 2의 제곱수
i = 0
while True:
    if N > 2**i:
        i += 1
    else:
        i += 1
        break

tree = [0] * (2**i)
nodeArr = [0] * (N+1)

init(1, 1, N)

for _ in range(M):
    a, b, c = list(map(int, input().split()))
    # 처음 입력이 0인경우
    if a == 0:
        if b > c:
            b, c = c, b
        print(sumTree(1, 1, N, b, c))
        continue
    # 처음 입력이 1인경우
    diff = c - nodeArr[b]
    nodeArr[b] = c
    update(1, 1, N, b, diff)