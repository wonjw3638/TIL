N, M = list(map(int, input().split()))

cnt = [0] * (N + 1)

for _ in range(M):
	arr = list(map(int, input().split()))
	n = arr[0]
	
	for i in range(1, n + 1):
		cnt[arr[i]] += 1

		
maxCnt = max(cnt)
answer = list()

cntRev = cnt.reverse()

for idx, n in enumerate(cnt):
	if n == maxCnt:
		answer.append(N-idx)

print(*answer)