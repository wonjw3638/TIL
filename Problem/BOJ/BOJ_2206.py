# 벽 부수고 이동하기
'''
14:07 ~ 14:31
14:55 ~
'''

def bfs():
    queue = [0] * (N * M)
    visited = [[[0] * M for _ in range(N)] for _ in range(2)]
    rear = front = -1
    rear += 1

    # i, j 좌표, 1cnt
    queue[rear] = [0, 0, 0]
    visited[0][0][0] = 1
    answer = N * M

    while front < rear:
        front += 1
        v = queue[front]

        for d in range(4):
            if (0 <= v[0] + di[d] < N) and (0 <= v[1] + dj[d] < M):
                # 이미 방문한 곳
                if visited[v[2]][v[0] + di[d]][v[1] + dj[d]] != 0:
                    continue
                else:
                    # 도착점 도착
                    if (v[0] + di[d] == N - 1) and (v[1] + dj[d] == M - 1):
                        return (visited[v[2]][v[0]][v[1]] + 1)

                    # 벽에 가로 막히면
                    if map_list[v[0] + di[d]][v[1] + dj[d]] == '1':
                        # 이미 벽 뿌신경우
                        if v[2] == 1:
                            continue
                        # 벽 안뿌신 경우
                        else:
                            rear += 1
                            visited[1][v[0] + di[d]][v[1] + dj[d]] = visited[0][v[0]][v[1]] + 1
                            queue[rear] = [v[0] + di[d], v[1] + dj[d], 1]
                            # visited[0][v[0] + di[d]][v[1] + dj[d]] = visited[0][v[0]][v[1]] + 1
                            # queue[rear] = [v[0] + di[d], v[1] + dj[d], 0]
                    else:
                        rear += 1
                        visited[v[2]][v[0] + di[d]][v[1] + dj[d]] = visited[v[2]][v[0]][v[1]] + 1
                        queue[rear] = [v[0] + di[d], v[1] + dj[d], v[2]]

    return -1

N, M = list(map(int, input().split()))
map_list = list()

for _ in range(N):
    map_list.append(input())

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

answer = bfs()

print(answer)