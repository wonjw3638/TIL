import sys
sys.setrecursionlimit(10**6)

N = int(input())
arr = [0] * (2 * N)
color = [2] * N
cnt = 0

def num(idx, color, arr):
    global cnt

    if idx == 2*N:
        cnt += 1
        if cnt == 100000007:
            cnt = 0
        return 
    
    for select in range(N):
        if select == arr[idx-1]:
            continue
        if color[select] == 0:
            continue
        if select > 0 and color[select-1] == 2:
            break

        color[select] -= 1
        arr[idx] = select
        num(idx+1, color, arr)
        color[select] += 1
        arr[idx] = 0
    return

color[0] -= 1
num(1, color, arr)

print(cnt%100000007)