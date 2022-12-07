# 3003 킹, 퀸, 룩, 비숍, 나이트, 폰 
# 221202

'''
시작시각 03:06
종료시각 03:08
'''

num = list(map(int, input().split()))
answer = list()

for idx, n in enumerate([1, 1, 2, 2, 2, 8]):
    answer.append(n - num[idx])

print(*answer)