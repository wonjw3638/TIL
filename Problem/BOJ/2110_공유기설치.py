# 2110 공유기 설치
# 220922

'''
16:54 ~ 
'''

N, C = list(map(int, input().split()))
arr = [int(input()) for _ in range(N)]
arr.sort()
arr_d = list()

for idx in range(N-1):
    arr_d.append(arr[idx+1] - arr[idx])

ans = (arr[-1] - arr[0])//(C-1)
answer = 987654321

tmp = 0
for d in arr_d:
    ttmp = tmp + d
    if ttmp > ans:
        answer = min(answer, tmp)
        tmp = d
        print('d:', d, 'tmp:', tmp)
    else:
        tmp += d

print(answer)