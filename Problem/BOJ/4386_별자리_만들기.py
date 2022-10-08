# 4386 별자리 만들기
# 220930

import sys, math
input = sys.stdin.readline

def find(x):
    if x != tree[x]:
        tree[x] = find(tree[x])
    return tree[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        tree[y] = x
    else:
        tree[x] = y


N = int(input())
tree = [ i for i in range(N) ] 
arr = [tuple(map(float, input().split())) for _ in range(N)]
wArr = list()

for i in range(N-1):
    for j in range(i+1, N):
        w = math.sqrt((arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2)
        wArr.append((i, j, w))

wArr.sort(key=lambda x : x[2])

answer = cnt = 0
for edge in wArr:
    node1, node2, w = edge
    if find(node1) != find(node2):
        union(node1, node2)
        answer += w
        cnt += 1
    
    if cnt == N-1:
        break

print(round(answer, 2))