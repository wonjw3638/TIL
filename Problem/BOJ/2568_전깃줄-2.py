from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
numbersArr = [list(map(int, input().split())) for _ in range(N)]
numbersArr.sort(key = lambda x: x[0])
numbers = [numbersArr[i][1] for i in range(N)]

# print(numbersArr)
# print(numbers)

Lis = list()
idx_list = list()

for i in numbers:
    k = bisect_left(Lis, i)
    idx_list.append(k)

    if len(Lis) <= k: 
        Lis.append(i)
    else:
        Lis[k] = i 


# print(Lis)
len_Lis = len(Lis)

print(N - len_Lis)
# idx_list.reverse()
# numbers.reverse()

answer = list()
len_Lis -= 1

# print(idx_list)
answer = list()
idx = N-1
while idx >= 0:
    # print(idx, idx_list[idx], len_Lis)
    if idx_list[idx] == len_Lis:
        len_Lis -= 1
    else:
        answer.append(numbersArr[idx][0])
    idx -= 1

for ans in answer[::-1]:
    print(ans)

# for idx in range(N):
#     print(idx_list[idx], len_Lis)
#     if idx_list[idx] == len_Lis:
#         len_Lis -= 1
#     else:
#         answer.append(numbersArr[idx][0])

# answer.reverse()

# print(*answer)