from collections import deque

n, m, k = map(int, input().split())

br_maps = dict()
for _ in range(m):
	a, b = map(int, input().split())
	if br_maps.get(a) == None:
		br_maps[a] = [b]
	else:
		br_maps[a].append(b)
		
q = deque()
q.append(k)

visited = dict()
for i in range(n+1):
	visited[i] = 0

while q:
	a = q.popleft()
	if br_maps.get(a) == None:
		continue
	else:
		for i in br_maps[a]:
			if visited[i] == 0:
				visited[i] = visited[a] + 1
				q.append(i)

if visited[k] == 0:
	print(-1)
else:
	print(visited[k])