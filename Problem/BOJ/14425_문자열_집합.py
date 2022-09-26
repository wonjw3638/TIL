# 14425 문자열 집합
# 220925

import sys
input = sys.stdin.readline

S = list()

N, M = list(map(int, input().split()))
S = [input() for _ in range(N)]

answer = 0
for _ in range(M):
    string = input()
    if string in S:
        answer += 1

print(answer)
