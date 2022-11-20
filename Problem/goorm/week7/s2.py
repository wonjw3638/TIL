from collections import deque

n = int(input())
m = int(input())

fr_maps = dict()
for _ in range(m):
	a, b = map(int, input().split())
	if fr_maps.get(a) == None:
		fr_maps[a] = [b]
	else:
		fr_maps[a].append(b)
	if fr_maps.get(b) == None:
		fr_maps[b] = [a]
	else:
		fr_maps[b].append(a)
		
if fr_maps.get(1) == None:
	print(1)
else:
	q = deque()
	q.append(1)

	visited = [False for _ in range(n+1)]
	visited[1] = True

	# print(q)
	while q:
		a = q.popleft()
		for i in fr_maps[a]:
			if not visited[i]:
				q.append(i)
				visited[i] = True

	ans = 0
	for i in range(1, n+1):
		if visited[i]:
			ans += 1

	print(ans)