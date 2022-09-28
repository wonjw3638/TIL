# 2887 행성 터널
# 220928

import sys
input = sys.stdin.readline

N = int(input())
arr = [[i] + list(map(int, input().split())) for i in range(N)]
edges = list()

for k in range(1, 4):
    arr.sort(key=lambda x : x[k])
    for idx in range(N-1):
        w = abs(arr[idx+1][k] - arr[idx][k])
        edges.append([w, arr[idx][0], arr[idx+1][0]])
        
edges.sort(key=lambda x : x[0])

answer = 0
# idx의 부모노드 표시하는 리스트
tree = [i for i in range(N)]
# idx를 부모로 가지는 자식노드 리스트
Ptree = [[i] for i in range(N)]

for edge in edges:
    # 다 같은 부모노드를 가질 때 멈춤
    if tree == tree[0] * N:
        break

    w, node1, node2 = edge
    Pnode1 = tree[node1]
    Pnode2 = tree[node2]

    if Pnode1 == Pnode2:
        continue
    else:
        answer += w
        if Pnode1 < Pnode2:
            for idx in Ptree[Pnode2]:
                tree[idx] = Pnode1
                Ptree[Pnode1].append(idx)
            Ptree[Pnode2] = []
        else:
            for idx in Ptree[Pnode1]:
                tree[idx] = Pnode2
                Ptree[Pnode2].append(idx)
            Ptree[Pnode1] = []

        
print(answer)
