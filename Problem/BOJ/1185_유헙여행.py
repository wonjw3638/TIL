# 1185 유럽여행
# 221004

'''
시작시각 04:54
종료시각
'''

import sys
input = sys.stdin.readline

N, P = list(map(int, input().split()))
arr = [0] + [int(input()) for _ in range(N)]
edge = list()

for _ in range(P):
    node1, node2, w = list(map(int, input().split()))
    edge.append([node1, node2, w+arr[node2]])
    edge.append([node2, node1, w+arr[node1]])
