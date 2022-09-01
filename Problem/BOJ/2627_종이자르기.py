W, M = list(map(int, input().split()))
N = int(input())

H = [0]
V = [0]

for _ in range(N):
    cutting = list(map(int, input().split()))
    if cutting[0] == 0:
        H.append(cutting[1])
    else:
        V.append(cutting[1])

H.append(M)
V.append(W)
H.sort()
V.sort()

cut_H = list()
tmp = H[0]
for h in H:
    cut_H.append(h-tmp)
    tmp = h

cut_V = list()
tmp = V[0]
for v in V:
    cut_V.append(v-tmp)
    tmp = v

print(max(cut_H) * max(cut_V))