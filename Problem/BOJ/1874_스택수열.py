# 1874 스택 수열
# 220927

import sys
input = sys.stdin.readline

N =  int(input())
arr = [ int(input()) for _ in range(N)]
stack = [0] * (N+1)
top = 0
stackNum = 1
answer = list()

for num in arr:
    # 같은 경우
    if stack[top] == num:
        # pop
        top -= 1
        answer.append('-')
    elif stack[top] < num:
        while stack[top] < num:
            # push
            top += 1
            stack[top] = stackNum
            answer.append('+')
            stackNum += 1
        # pop
        top -= 1
        answer.append('-')
    else:
        print('NO')
        break
else:
    for ans in answer:
        print(ans)