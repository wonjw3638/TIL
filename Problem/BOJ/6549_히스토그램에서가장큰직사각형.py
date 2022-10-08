# 6549 히스토그램에서 가장 큰 직사각형
# 221002


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def init(node, s, d):
    if s == d:
        tree[node] = s
        return tree[node]

    mid = (s+d)//2
    idx1 = init(node*2, s, mid)
    idx2 = init(node*2 + 1, mid+1, d)

    if arr[idx1] < arr[idx2]:
        tree[node] = idx1
    else:
        tree[node] = idx2

    return tree[node]

# 최소 인덱스 -> 높이값 찾기
def findMin(node, s, d, l, r):
    if d < l or r < s:
        return -1

    if l <= s and d <= r:
        return tree[node]
    else:
        mid = (s+d)//2
        idx1 = findMin(node*2, s, mid, l, r)
        idx2 = findMin(node*2 + 1, mid+1, d, l, r)

        if idx1 == -1:
            return idx2
        elif idx2 == -1:
            return idx1
        else:
            if arr[idx1] < arr[idx2]:
                return idx1
            else:
                return idx2

# idx l~r 직사각형 중에서 가장 작은 index * 구간 가로 길이 (r-l+1)
def maxArea(l, r):
    if l == r:
        return arr[l]
    
    minIdx = findMin(1, 1, N, l, r)

    area = arr[minIdx] * (r-l+1)

    if l <= minIdx-1:
        area1 = maxArea(l, minIdx-1)
        if area < area1:
            area = area1
    if minIdx+1 <= r:
        area2 = maxArea(minIdx+1, r)
        if area < area2:
            area = area2

    return area

while True:
    inputList = list(map(int, input().split()))
    if inputList == [0]:
        break

    N = inputList[0]
    arr = [0] + inputList[1:]

    i = 0
    while True:
        if N > 2**i:
            i += 1
        else:
            i += 1
            break

    tree = [0] * (2**i)

    # 세그먼트 트리에 구간별 최소 높이를 가지는 블럭의 idx 저장
    init(1, 1, N)

    # 정답 변수
    answer = maxArea(1, N)

    print(answer)