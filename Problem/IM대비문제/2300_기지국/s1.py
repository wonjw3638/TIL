# BOJ 2300_기지국
# 220818
'''
설계 14:35 ~ 14:51
구현 15:05 ~ 17:00
시간초과 ~! 
'''

import sys
sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

N = int(input())
node_info = list()

for _ in range(N):
    x, y = list(map(int, input().split()))
    node_info.append([x, y])

# 기지국 x좌표 기준으로 정렬
node_info.sort()


# 필요한 통신범위 계산
def cal(pos_list):
    n = len(pos_list)
    x_min = min(pos_list[i][0] for i in range(n))
    x_max = max(pos_list[i][0] for i in range(n))
    y_max = max(abs(pos_list[i][1]) for i in range(n))
    max_val = max((x_max - x_min),(2 * y_max))
    return max_val

min_table = [[] for _ in range(N+1)]
min_table[0] = abs(node_info[0][1] * 2)
# 기지국 설치개수
for j in range(1, N+1):
    q = 1000001
    for i in range(j-1):
        q = min(q, min_table[i] + cal(node_info[i:j]))
    min_table[j] = q

print(min_table[N-1])