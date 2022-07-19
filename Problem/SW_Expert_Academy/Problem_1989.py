T = int(input())
for case in range(1,T+1):
    check = True
    word = str(input())
    lens = len(word)
    for i in range(0,lens//2+1):
        if word[i] == word[lens-1-i]:
            continue
        else:
            check = False
            break
    if check == True:
        print(f'#{case} 1')
    else: print(f'#{case} 0')