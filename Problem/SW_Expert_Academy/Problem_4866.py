import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(1, t+1):
    arr = list(input()) # 리스트로 받기
    stack_list = [] # 스택 리스트 만들기
    open_list = ['(', '{']
    close_list = [')', '}']
    dic = {
        ')' : '(',
        '}' : '{',
    }
    answer = 1
    for i in arr:   # 리스트 인자 하나씩 보기
        if i in open_list:
            stack_list.append(i)
            continue
        if i in close_list:
            if not stack_list:
                answer = 0
                break
            if stack_list.pop(-1) == dic.get(i):
                continue
            else:
                answer = 0
                break

    if stack_list:
        answer = 0

    print('#{} {}'.format(tc, answer))