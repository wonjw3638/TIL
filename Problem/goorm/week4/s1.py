N, M = list(map(int, input().split()))
stack = list()

for _ in range(M):
    string, k = list(input().split())
    k = int(k)
    if string == 'deposit':
        N += k
    elif string == 'pay':
        if N - k >= 0:
            N -= k
    else:
        if stack:
            stack.append(k)
        else:
            if N >= k:
                N -= k
            else:
                stack.append(k)
    while stack:
        if N >= stack[0]:
            N -= stack[0]
            stack.pop(0)
        else:
            break

print(N)