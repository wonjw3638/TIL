# 11723 집합 
# 221208

'''
시작시각 02:43
종료시각 03:00
'''

import sys
input = sys.stdin.readline

# 연산의 수 M
M = int(input())

# 공집합 S
S = [False] * 21

for _ in range(M):
    # 연산 입력 받기
    msg = input().strip()
    # 연산 값이 all일 때 -> 전부 True
    if msg == 'all':
        S = [True] * 21
    # 연산 값이 empty일 때
    elif msg =='empty':
        S = [False] * 21
    # 연산 값이 all, empty가 아닐 때
    else:
        # n을 정수형으로 변환
        msg, n = msg.split()
        n = int(n)
        # 연산 값이 add일 때
        if msg == 'add':
            if S[n] == False:
                S[n] = True
        # 연산 값이 remove일 때
        if msg == 'remove':
            if S[n] == True:
                S[n] = False
        # 연산 값이 check일 때
        if msg == 'check':
            if S[n] == True:
                print(1)
            else:
                print(0)
        # 연산 값이 toggle일 때
        if msg == 'toggle':
            if S[n] == True:
                S[n] = False
            else:
                S[n] = True