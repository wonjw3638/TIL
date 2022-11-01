from collections import deque


N = int(input())
tree = [[] for _ in range(N+1)]
cnt = [0] * (N+1)

for _ in range(N):
	node1, node2 = list(map(int, input().split()))
	tree[node1].append(node2)
	tree[node2].append(node1)
	cnt[node1] += 1
	cnt[node2] += 1

queue = deque()

print(tree)
print(cnt)

for idx, ct in enumerate(cnt):
	if ct == 1:
		queue.append(idx)

visited = [0] * (N+1)

while queue:
	idx = queue.popleft()
	cnt[idx] -= 1
	visited[idx] = 1
	
	print(idx)
	print(cnt)
	
	for idx2 in tree[idx]:
			if visited[idx2] == 0:
					cnt[idx2] -= 1
					if cnt[idx2] == 1:
							queue.append(idx2)

answer = list()			
			
for idx, node in enumerate(cnt):
	if node != 0:
		print(idx, node)
		answer.append(idx)

print(len(answer))
print(*answer)