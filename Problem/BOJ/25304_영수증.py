# 25304 영수증

'''
시작시각 03:37
종료시각
'''

# 영수증에 적힌 총 금액 X
X = int(input())

# 구매한 물건의 종류의 수 N
N = int(input())

# 구매한 총 금액
total = 0

# N개의 물건 가격 a, 개수 b
# N번 반복하면서 a*b 값을 전체 값에 더해감
for _ in range(N):
    a, b = map(int, input().split())
    total += a * b

if X == total:
    print('Yes')
else:
    print('No')