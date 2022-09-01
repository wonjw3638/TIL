C, R = list(map(int, input().split()))
N = int(input())
mapList = [[0] * C for _ in range(R)]

def check():
    if N > C * R:
        return [0]

    i = R
    j = direction = 0
    num = 1

    while num <= N:
        if direction == 0:
            ni = i-1
            nj = j
        elif direction == 1:
            ni = i
            nj = j+1
        elif direction == 2:
            ni = i+1
            nj = j
        else :
            ni = i
            nj = j-1
        
        if (0 <= ni < R) and (0 <= nj < C):
            if mapList[ni][nj] != 0:
                direction = (direction + 1) % 4
                continue
            else:
                mapList[ni][nj] = num
                num += 1
                i = ni
                j = nj
                continue
        else:
            direction = (direction + 1) % 4
            continue

    return [j + 1, R - i]

answer = check()
print(*answer)