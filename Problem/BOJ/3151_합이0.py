# 3151 합이 0
# 220925
from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0

for idx in range(N-2):
    num = -arr[idx]
    start = idx+1
    end = N-1
    while start < end:
        total = arr[start] + arr[end]
        if total == num:
            if arr[start] == arr[end]:
                answer += end - start
            else:
                i = bisect_left(arr, arr[end])
                answer += end-i+1
            start += 1
        elif total > num:
            end -= 1
        else:
            start += 1

print(answer)