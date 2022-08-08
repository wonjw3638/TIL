# 1206_view
# 220808

import sys
sys.stdin = open('input.txt','r')

def my_max(a):  # 최대값 구하는 함수
    tmp = 0
    for i in a:
        if i > tmp:
            tmp = i
        else:
            continue
    return tmp

for tc in range(1,11):
    answer = 0
    T = int(input())
    buding = list(map(int, input().split()))
    for idx in range(0,T-4):
        building_check = buding[idx:idx+5]  # 5개의 빌딩 높이 값
        idx3 = building_check.pop(2)        # 가장 가운데 있는 값 뽑기, 제외
        building_max = my_max(building_check)  # 가장 가운데 있는 빌딩을 제외한 빌딩 중에 가장 높은 빌딩 값
        if building_max < idx3:       # 가운데 빌딩이 가장 크다면 그 차이만큼 더하기
            answer += (idx3 - building_max)

    print(f'#{tc} {answer}')