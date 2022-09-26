# 2473 세용액
# 220924

'''
시작시각 12:46 
종료시각 12:57
''' 

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 3000000000

for idx in range(N-2):
    startIdx = idx+1
    endIdx = N-1


    while startIdx < endIdx:
        total = arr[idx] + arr[startIdx] + arr[endIdx]
        
        if abs(total) < answer:
            answer = abs(total)
            answer_arr = [arr[idx], arr[startIdx], arr[endIdx]]
        
        if total > 0:
            endIdx -= 1
        elif total < 0:
            startIdx += 1
        else:
            break
    
    if answer == 0:
        break

print(*answer_arr)