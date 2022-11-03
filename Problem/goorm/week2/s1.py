t = int(input())
for tc in range(t):
	n = int(input())
	v = list(map(int, input().split()))
	
	avg = sum(v)/n
	cnt = 0
	for score in v:
		if score >= avg:
			cnt += 1
	
	print(f'{cnt}/{n}')
