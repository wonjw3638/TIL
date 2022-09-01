# N = int(input())
# arr = list(map(int, input().split()))

# answer = cnt = 0

# tmp = arr[0]
# for num in arr:
#     if num - tmp >= 0:
#         cnt += 1
#         tmp = num
#     else:
#         if cnt > answer:
#             answer = cnt
#         cnt = 1
#         tmp = num
# if cnt > answer:
#     answer = cnt

# cnt = 0
# tmp = arr[-1]
# for num in arr[::-1]:
#     if num - tmp >= 0:
#         cnt += 1
#         tmp = num
#     else:
#         if cnt > answer:
#             answer = cnt
#         cnt = 1
#         tmp = num
# if cnt > answer:
#     answer = cnt

# print(answer)

N = int(input())
arr = list(map(int, input().split()))
dp1, dp2 = [1] * N, [1] * N

for i in range(1, N):
    
    if arr[i] <= arr[i-1]:
        dp1[i] =  dp1[i-1] + 1
        
    if arr[i] >= arr[i-1]:
        dp2[i] =  dp2[i-1] + 1
        
print(max(max(dp1), max(dp2)))