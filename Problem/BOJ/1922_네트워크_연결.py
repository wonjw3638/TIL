# 1992 네트워크 연결
# 220927

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# 간선 정보 저장
arr = list()

for _ in range(M):
    node1, node2, w = list(map(int, input().split()))
    # 가중치, node1, node2 순서로 저장
    arr.append([w, node1, node2])

# 가중치 오름차순으로 정렬
arr.sort(key= lambda x : x[0])

# 선택한 간선들로 만들 새로운 트리 정보, 가중치 가장 작은 간선은 무조건 선택
newTree = [[]]
answer = 0

# print(arr)

# 간선 선택
for edge in arr:
    # 모든 간선 연결하면 break
    if len(newTree[0]) == N:
        break
    # 부모노드 타고 올라가서 본인이 나오는지 확인
    # 본인 노드가 나오면 그 간선은 선택x, 다음으로 작은 가중치를 가지는 노드 확인
    w, node1, node2 = edge
    if node1 == node2:
        continue
    check1 = check2 = False
    listIdx1 = listIdx2 = -1
    for idx, tree in enumerate(newTree):
        if node1 in tree:
            check1 = True
            listIdx1 = idx

        if node2 in tree:
            check2 = True
            listIdx2 = idx

        # 간선 선택 x
        if listIdx1 != -1 and listIdx1 == listIdx2:
            break
        
        if check1 == True and check2 == True:
            break

    # 간선 선택하는 경우
    if check1 == True and check2 == False:
        answer += w
        if listIdx1>0:
            newTree[listIdx1].append(node2)
    elif check2 == True and check1 == False:
        answer += w
        if listIdx2>0:
            newTree[listIdx2].append(node1)
    elif check1 == False and check2 == False:
        answer += w
        newTree.append([node1, node2])
    elif ((check1 == True) and (check2 == True)) and (listIdx1 != listIdx2):
        answer += w
        if listIdx1>0 and listIdx2>0:
            newTree[listIdx1] += newTree[listIdx2]
            newTree[listIdx2] = list()
    else:
        continue

print(answer)