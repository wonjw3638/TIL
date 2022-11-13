import sys
sys.setrecursionlimit(10**6)

N = int(input())
cnt = 0

di = [-1, 0]
dj = [0, -1]
arr = [[0] * 3 for _ in range(N)]

def sticker(i, j):
    global cnt

    if i == N:
        cnt += 1
        return 

    for d in range(2):
        if 0 <= i + di[d] < N and 0 <= j + dj[d] < 3:
            if arr[i + di[d]][j + dj[d]] == 1:
                break
    else:
        arr[i][j] = 1
        if j == 2:
            sticker(i+1, 0)
        else:
            sticker(i, j+1)
        arr[i][j] = 0
    if j == 2:
        sticker(i+1, 0)
    else:
        sticker(i, j+1)
    
        
sticker(0, 0)

print(cnt%100000007)


    
