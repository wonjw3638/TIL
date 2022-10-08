# 2342 Dance Dance Revolution
# 221001

arr = [0] + list(map(int, input().split()))
N = len(arr)
inf = float('INF')
# idx번째 발판, 왼쪽발, 오른쪽발 위치
dp = [[[inf] * 5 for _ in range(5)] for _ in range(N-1)]

power = {
    0 : [inf, 2, 2, 2, 2],
    1 : [inf, 1, 3, 4, 3],
    2 : [inf, 3, 1, 3, 4],
    3 : [inf, 4, 3, 1, 3],
    4 : [inf, 3, 4, 3, 1],
}

# 처음 위치 0, 0
dp[0][0][0] = 0

# N까지 하니까 마지막 0도 이동해서 빼줌
for idx in range(1, N-1):
    for i in range(5):
        for k in range(5):
            # 왼쪽발이 arr[idx]로 갈때 최소값
            dp[idx][arr[idx]][i] = min(dp[idx][arr[idx]][i], dp[idx-1][k][i] + power.get(k)[arr[idx]])
            # 오른쪽발이 arr[idx]로 갈때 최소값
            dp[idx][i][arr[idx]] = min(dp[idx][i][arr[idx]], dp[idx-1][i][k] + power.get(k)[arr[idx]])

answer = min(map(min, dp[-1]))
print(answer)