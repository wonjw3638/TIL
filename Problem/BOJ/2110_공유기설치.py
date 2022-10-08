# 2110 공유기 설치
# 220922

N, C = list(map(int, input().split()))
arr = [int(input()) for _ in range(N)]
arr.sort()
numArr = list()

for idx in range(N-1):
    numArr.append(arr[idx+1] - arr[idx])

# 최솟값, 최댓값 설정
start = min(numArr)
end = max(numArr)
answer = 0

while start <= end:
    mid = (start + end)//2
    idx = tmp = cnt = 0

    while idx < N-1:
        print(start, end, idx)
        if numArr[idx] >= mid:
            cnt += 1
            tmp = 0
        else:
            tmp += numArr[idx]
            if tmp >= mid:
                cnt += 1
                tmp = 0
        idx += 1
    
    if cnt > C:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1 

print(answer)