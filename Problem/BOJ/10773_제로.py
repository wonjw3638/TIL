# 10773 제로
# 221206

'''
시작시각 22:49
종료시각 22:55
'''

import sys
input = sys.stdin.readline

# 받는 정수 개수
K = int(input())
# 최종 합의 값
answer = 0
# 저장해둘 이전 값
pre = list()

# 반복문을 통해 입력 값을 받음, 최종 값에 더하고 이전 값에 저장해둠
for _ in range(K):
    n = int(input())
    # n값이 0인 경우 이전 마지막 값을 뺌
    if n == 0:
        answer -= pre.pop()
        continue
    answer += n
    pre.append(n)

print(answer)