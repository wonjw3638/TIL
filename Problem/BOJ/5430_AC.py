# 5430 AC
# 221003

'''
시작시각 19:41~
종료시각
'''

import sys
input = sys.stdin.readline
from collections import deque


T = int(input())

for tc in range(1, T+1):
    p = input()
    n = int(input())

    arrString = input().rstrip()
    arr = deque(arrString[1:-1].split(','))
    rev = False

    for func in p:
        if func == 'R':
            if rev == True:
                rev = False
            else:
                rev = True

        elif func == 'D':
            if n > 0:
                n -= 1
                if rev == False:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print('error')
                break
    else:
        if rev == True:
            print('[' + ','.join(list(arr)[::-1]) + ']')
        else:
            print('[' + ','.join(list(arr)) + ']')