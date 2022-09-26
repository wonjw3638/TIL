# 1436 영화감독숌
# 220925

N = int(input())

n = 666
idx = 1

while True:
    if idx == N:
        answer = n
        break
    else:
        n += 1
        if '666' in str(n):
            idx += 1

print(answer)
