# 9935 문자열 폭발
# 221002

mainString = input()
findString = list(input())

N = len(findString)       
stack = list()

for char in mainString:
    stack.append(char)
    if char == findString[-1] and findString == stack[-N:]:
        for _ in range(N):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")