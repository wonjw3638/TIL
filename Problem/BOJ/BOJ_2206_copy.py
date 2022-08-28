from copy import deepcopy


def bfs(a):
    queue = [0] * (N * M)
    visited = [[0] * M for _ in range(N)]
    rear = front = -1
    rear += 1

    # i, j 좌표, 거리, 1cnt
    queue[rear] = [0, 0, 1]
    visited[0][0] = 1
    answer = N * M

    while front < rear:
        front += 1
        v = queue[front]

        for d in range(4):
            if (0 <= v[0] + di[d] < N) and (0 <= v[1] + dj[d] < M):
                if visited[v[0] + di[d]][v[1] + dj[d]] == 1:
                    continue
                else:
                    # 도착점 도착
                    if (v[0] + di[d] == N - 1) and (v[1] + dj[d] == M - 1):
                        tmp = v[2] + 1
                        if tmp < answer:
                            answer = tmp
                    else:
                        if a[v[0] + di[d]][v[1] + dj[d]] == '1':
                            continue
                        else:
                            rear += 1
                            visited[v[0] + di[d]][v[1] + dj[d]] = 1
                            queue[rear] = [v[0] + di[d], v[1] + dj[d], v[2] + 1]
    
    if answer == N * M:
        return 9999
    else:
        return answer


N, M = list(map(int, input().split()))
map_list = list()

for _ in range(N):
    map_list.append(list(input()))

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]


# 기본형태
answer = bfs(map_list)

for i in range(N):
    for j in range(M):
        if map_list[i][j] == '1':
            for d in range(2):
                if (0 <= i + di[d] < N) and (0 <= j + dj[d] < M):
                    if (0 <= i + di[d + 2] < N) and (0 <= j + dj[d + 2] < M):
                        if map_list[i + di[d]][j + dj[d]] == map_list[i + di[d + 2]][j + dj[d + 2]] == '0':
                            map_list_tmp = deepcopy(map_list)
                            map_list_tmp[i][j] = '0'
                            tmp = bfs(map_list_tmp)
                            if tmp < answer:
                                answer = tmp

if answer == 9999:
    answer = -1

print(answer)