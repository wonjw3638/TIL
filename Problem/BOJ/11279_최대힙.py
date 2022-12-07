# 11279 최대힙
# 221205

'''
시작시각 02:15
종료시각
'''

# heapq, readline import
import heapq
import sys
input = sys.stdin.readline

# 연산의 개수 N
N = int(input())

# 값을 저장할 배열 list
arr = list()

for _ in range(N):
    x = int(input())
    # x가 0인 경우
    if x == 0:
        # 배열이 비어있는 경우에는 0출력
        if not arr:
            print(0)
        # 배열에 값이 있다면 가장 작은 값 반환. 후에 -1 곱하면 원했던 큰 값 반환.후 삭제 - heappop
        else:
            print(-heapq.heappop(arr))
    # x가 자연수인 경우 -> -1을 곱한 상태로 저장. - heappush
    else:
        heapq.heappush(arr, -x)