# 1197 최소 스패닝 트리
# 220928

'''
시작시각 01:28
종료시각 01:42
'''

import sys
input = sys.stdin.readline

# 정점의 개수, 간선의 개수
V, E = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(E)]
arr.sort(key=lambda x : x[2])

tree = [i for i in range(V+1)]
answer = 0

for edge in arr:
    # 모든 노드가 하나로 연결된 경우
    if tree[1:] == tree[1] * V:
        break

    node1, node2, w = edge
    Pnode1 = tree[node1]
    Pnode2 = tree[node2]

    # 같은 부모노드를 가지고 있으면 넘김
    if Pnode1 == Pnode2:
        continue
    else:
        answer += w
        # 더 작은 것을 부모노드로 선택, 합쳐주기
        if Pnode1 > Pnode2:
            tree[node1] = Pnode2
            for idx in range(1, V+1):
                if tree[idx] == Pnode1:
                    tree[idx] = Pnode2
        else:
            tree[node2] = Pnode1
            for idx in range(1, V+1):
                if tree[idx] == Pnode2:
                    tree[idx] = Pnode1


print(answer)