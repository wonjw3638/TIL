# SWEA 1952_수영장
# 220819
'''
설계 12:59 ~ 1:05
구현 1:06 ~ 18, 43~14:50

배낭용량 = 개월 수 = 12
짐의 용량 = 이용 가능 개월 수 
짐의 가치 = 가격
최대 12개 넣는 거 가능. 최소 가치를 갖는 방법 찾기.

&&&
브루트 포스 방식 고려하기
&&&&

'''

import sys
sys.stdin = open('input.txt','rt')
input = sys.stdin.readline

T = int(input())

for tc in range(1, 2):
    # 1일 1달 3달 1년
    fee_month = [1, 1, 3, 12]
    fee = list(map(int, input().split()))
    month = list(map(int, input().split()))

    # 월별 최적의 요금 값
    min_month = [0] * 13
    acc_min_val = [0] * 13
    min_month2 = [0] * 13

    # m월에 대한 최적의 요금 찾기
    for m in range(1, 13):
        # 1일권, 1달권 사용값 비교, min_month에 업데이트
        minVal = min(month[m-1] * fee[0] , fee[1])
        min_month[m] = minVal
        acc_min_val[m] = acc_min_val[m-1] + minVal

    print(min_month)
    print(acc_min_val)

    # 3달권도 사용할때 값 비교
    for m in range(1, 13):
        q = 3001
        for j in range(1, m+1):
            print(m-j, q, acc_min_val[m-j] , fee[2])
            q = min(q, (acc_min_val[m-j] + fee[2]))
        min_month2[m] = q

    print('#{} {}'.format(tc, min_month2[12]))
