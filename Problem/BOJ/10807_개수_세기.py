# 10807 개수 세기


'''
시작시각 03:46
종료시각 03:47
'''

# 정수의 개수 N
N = int(input())

# 정수 배열
arr = list(map(int, input().split()))

# 찾으려고 하는 정수 v
v = int(input())

print(arr.count(v))