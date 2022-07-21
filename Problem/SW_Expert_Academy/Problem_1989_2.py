T = int(input())
T_reverse = T[::-1]
if T == T_reverse:
    print(f'#{case} 1')
else: print(f'#{case} 0')