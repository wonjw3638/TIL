N = int(input())

def SUB(num):
    idx = 0
    numbers = [N, num]
    while True:
        tmp = numbers[idx] - numbers[idx + 1]
        if tmp >= 0:
            numbers.append(tmp)
            idx += 1
        else:
            break
    return numbers

answer = answer_cnt = 0

for i in range(1, N + 1):
    tmp = SUB(i)
    if len(tmp) > answer_cnt:
        answer_cnt = len(tmp)
        answer = tmp

print(answer_cnt)
print(*answer)