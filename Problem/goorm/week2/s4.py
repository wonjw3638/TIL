n, k = list(map(int, input().split()))
arr = [[0] * (n+1) for _ in range(n+1)]

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, 1, -1]

answer = 0

for _ in range(k):
	a, b = list(map(int, input().split()))
	
	for d in range(5):
		if 0 < a + di[d] <= n and 0 < b + dj[d] <= n:
			answer += 1

print(answer)