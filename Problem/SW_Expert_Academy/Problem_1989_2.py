T = int(input())
for case in T:
    string = input()
    r_string = T[::-1]
    if string == r_string:
        print(f'#{case + 1} 1')
    else: print(f'#{case + 1} 0')