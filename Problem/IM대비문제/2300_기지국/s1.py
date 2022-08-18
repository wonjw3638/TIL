# BOJ 2300_기지국
# 220818
'''
설계 14:35 ~ 14:51
구현 15:05 ~ 17:00 + 1h
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

# x_min, x_max, y_max  메모이제이션
cal_list = []

# 필요한 통신범위 계산
def cal(a,b):
    if a == b-1:
        cal_list.append([node_info[a][0], node_info[a][0], abs(node_info[a][1])])
        return ( 2 * cal_list[a][2])
    else:
        x_min = min(cal_list[a][0], cal_list[b-1][0])
        x_max = max(cal_list[a][1], cal_list[b-1][1])
        y_max = max(cal_list[a][2], cal_list[b-1][2])
        cal_list[a] = [x_min, x_max, y_max]
        return max((x_max - x_min),(2 * y_max))

# 최적의 값을 저장할 list
min_table = [0] * (N+1)

# 기지국 설치개수
for j in range(1, N+1):
    # 큰 값으로 설정
    q = 1000001
    for i in range(1, j+1):
        calcul = cal(j-i,j)
        if calcul > q: 
            continue
        else:
            q = min(q, calcul + min_table[j-i])
    min_table[j] = q

print(min_table[N])