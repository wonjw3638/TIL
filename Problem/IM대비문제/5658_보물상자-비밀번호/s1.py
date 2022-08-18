# SWEA 5658_보물상자 비밀번호
# 220818
'''
설계 17:05 ~ 17:09
구현 17:10 ~ 17:35
'''

import sys
sys.stdin = open('input.txt','rt')

T = int(input())

# 10진수 초과 알파벳 대응하는 딕셔너리
hex_dict = {
    'A' : 10,
    'B' : 11,
    'C' : 12,
    'D' : 13,
    'E' : 14,
    'F' : 15,
}

# 16진수 -> 10진수로 바꿔주는 함수
def hex_dec(string):
    answer = 0
    for i, s in enumerate(string[::-1]):
        if s in hex_dict:
            answer += hex_dict.get(s) * (16**i)
        else:
            answer += int(s) * (16**i)
    return answer

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    n = N//4
    num_list = list()
    string = input()

    # 가능한 문자열 받기, 중복 제거
    first = string
    while True:
        if not num_list:
            for i in range(0, N, n):
                num_list.append(string[i:i+n])
                string = string[1:] + string[0]
        else:
            if string == first:
                break
            else:
                for i in range(0, N, n):
                    num_list.append(string[i:i+n])
                string = string[1:] + string[0]
    num_list = set(num_list)
    num_list = list(map(hex_dec, num_list))
    M = len(num_list)

    # 버블소트 정렬 K번째로 큰게 궁금하니까 K까지만 정렬
    for i in range(K):
        maxIdx = i
        for j in range(i+1, M):
            if (num_list[maxIdx]) < (num_list[j]):
                maxIdx = j
        num_list[maxIdx], num_list[i] = num_list[i], num_list[maxIdx]

    print('#{} {}'.format(tc, num_list[K-1]))