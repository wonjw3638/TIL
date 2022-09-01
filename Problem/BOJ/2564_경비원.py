N, M = list(map(int, input().split()))
S = int(input())

stores = [list(map(int, input().split())) for _ in range(S)]
security = list(map(int, input().split()))

direction = {
    1 : 2,
    2 : 1,
    3 : 4,
    4 : 3,
}

answer = 0

for store in stores:
    if store[0] == security[0]:
        answer += abs(security[1] - store[1])
    elif security[0] == direction.get(store[0]):
        if security[0] in [1, 2]:
            tmp1 = security[1] + M + store[1]
            tmp2 = (2 * N) - security[1] + M - store[1]
            answer += min(tmp1, tmp2)
        else:
            tmp1 = security[1] + N + store[1]
            tmp2 = (2 * M) - security[1] + N - store[1]
            answer += min(tmp1, tmp2)
    else:
        if security[0] == 1:
            if store[0] == 3:
                answer += security[1] + store[1]
            else:
                answer += N - security[1] + store[1]
        elif security[0] == 2:
            if store[0] == 3:
                answer += security[1] + M - store[1]
            else:
                answer += N - security[1] + M - store[1]
        elif security[0] == 3:
            if store[0] == 1:
                answer += security[1] + store[1]
            else:
                answer += M - security[1] + store[1]
        else:
            if store[0] == 1:
                answer += N - store[1] + security[1]
            else:
                answer += M - security[1] + N - store[1]

print(answer)

