import sys
input = sys.stdin.readline

N = int(input())

map_list = [[0] * 1001 for _ in range(1001)]

paper = list()
answer = list()

for _ in range(N):
    paper.append(list(map(int, input().split())))

for idx in range(N-1, -1, -1):
    x, y, w, h = paper[idx]
    tmp = 0
    for j in range(w):
        for i in range(h):
            if map_list[y+i][x+j] > 0:
                continue
            else:
                map_list[y+i][x+j] = 1
                tmp += 1
    answer.append(tmp)

for idx in range(N-1, -1, -1):
    print(answer[idx])

        

# for n in range(1, N+1):
#     x1, y1, w, h = list(map(int, input().split()))
#     for i in range(y1, y1+h):
#         map_list[i][x1:x1+w] = [n] * w

#     # for i in range(h):
#     #     for j in range(w):
#     #         map_list[y1 + i][x1 + j] = n

# for n in range(1, N+1):
#     tmp = 0
#     for i in range(1001):
#         for j in range(1001):
#             if map_list[i][j] == n:
#                 tmp += 1
#     print(tmp)
