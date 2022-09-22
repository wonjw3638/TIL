# 1654 랜선 자르기
# 220922

'''
16:30 ~ 16:50
'''

K, N = list(map(int, input().split()))
arr = [int(input()) for _ in range(K)]

start = 1
end = sum(arr)//N

while True:
    mid = (start + end) // 2
    cnt = 0
    for ar in arr:
        cnt += ar//mid

    if cnt >= N:
        if start == mid or end == mid:
            cnt = 0
            for ar in arr:
                cnt += ar//end
            if cnt >= N:
                answer = end
                break
            else:
                answer = start
                break
        else:
            start = mid
            continue
    else:
        end = mid
        continue

print(answer)