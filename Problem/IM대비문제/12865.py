# 12865 평범한 배낭
'''

'''
# 담을 수 있는 물품의 수, 버틸 수 있는 무게
N, K = list(map(int, input().split()))
W = list() # 물건의 무게
V = list() # 물건의 가치

for _ in range(N):
    w, v = list(map(int, input().split()))
    W.append(w)
    V.append(v)

pack = []

for i in range(N+1):
    pack.append([])
    for c in range(K+1):
        if i == 0 or c == 0:
            pack[i].append(0)
        elif 
