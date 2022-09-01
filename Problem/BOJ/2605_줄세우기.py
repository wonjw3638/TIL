N = int(input())
line = list(map(int, input().split()))
student = [i for i in range(1, N + 1)]

for idx in range(N):
    if line[idx] == 0:
        continue
    else:
        student.insert(idx - line[idx], student.pop(idx))

print(*student)