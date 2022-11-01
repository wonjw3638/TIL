# 9095 1,2,3 더하기
# 221202

'''
시작시각 02:32
종료시각 02:42
'''


def find(n, string):
    if n == 0:
        if not string in answer:
            answer.append(string)
        return 
    
    for num in [1, 2, 3]:
        if n >= num:
            find(n-num, string + str(num))
        else:
            continue

T = int(input())
for _ in range(T):
    answer = list()
    N = int(input())

    find(N, '')

    print(len(answer))
