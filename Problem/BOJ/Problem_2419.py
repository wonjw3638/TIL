max_cnt = 0
cnt = 1
com = True # true 증가 false 감소
temp = -1


N = int(input())
numbers = map(int, input().split())

for num in numbers:
    print(f'num, cnt : {num}, {cnt}')
    if cnt == 0:
        temp = num
        continue
    
    if temp == num :
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
        continue

    elif temp < num :
        if com == True:
            cnt += 1
            temp = num
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            com = True
            temp = num
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 1

    elif temp > num :
        if com == False:
            cnt += 1
            temp = num
            if cnt > max_cnt:
                max_cnt = cnt        
        else:
            com = True
            temp = num
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 1

print(max_cnt)
## 아직 푸는 중