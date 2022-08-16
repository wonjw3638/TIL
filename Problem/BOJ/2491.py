N = int(input())
num_list = list(map(int, input().split()))

# 증가, 일정, 감소
cnt = [0] * 3 
tmp = -1

def check(num_list, i):
    idx = 0
    cnt = 1
    check = None
    while idx + i < N-1 :
    # 증가
        if num_list[idx] < num_list[idx + 1]:
            if (check == True) or (check == None):
                cnt += 1
                idx += 1
                check = True
            else:
                return cnt
        # 감소
        elif num_list[idx] > num_list[idx + 1]:
            if (check == False) or (check == None):
                cnt += 1
                idx += 1
                check = False
            else:
                return cnt
        # 일정
        else:
            cnt += 1
            idx += 1

    return cnt
    
max_cnt = 0
for i in range(N):
    cnt = check(num_list[i:], i)
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt) 