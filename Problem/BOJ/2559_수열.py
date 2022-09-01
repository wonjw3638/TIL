N, K = list(map(int, input().split()))
num_list = list(map(int, input().split()))

start_idx = 0
end_idx = K
answer = tmp = sum(num_list[:K])

for _ in range(N-K):
    tmp = tmp - num_list[start_idx] + num_list[end_idx]
    if tmp > answer:
        answer = tmp
    start_idx += 1
    end_idx += 1

print(answer)