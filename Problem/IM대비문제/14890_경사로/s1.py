# SWEA 14890_경사로
# 220819
'''
설계 09:40 ~ 09:45
구현   ~~ 11:40
'''

N, L = list(map(int, input().split()))

map_list = list()

for _ in range(N):
    map_list.append(list(map(int, input().split())))

answer = 0

# 행 탐색
for i in range(N):
    tmp = map_list[i][0]
    # slope 경사 1 -> 오르막, -1 -> 내리막
    tmp_cnt = slope = 0 
    down_check = False
    for j in range(N):
        
        sub = tmp - map_list[i][j]
        # 같은 값인 경우
        if sub == 0:
            tmp_cnt += 1
        elif abs(sub) < 2 :
            # 오르막
            if sub < 0:
                # 원래 내리막이었던 경우
                if slope == -1:
                    # 나왔던 값들의 개수가 L보다 커야함 (하나는 내리막용 경사)
                    if tmp_cnt >= 2 * L:
                        tmp = map_list[i][j]
                        tmp_cnt = 1
                        slope = 1
                    else: break
                # 원래 평지/오르막이었던 경우
                else:
                    if tmp_cnt >= L:
                        tmp = map_list[i][j]
                        tmp_cnt = 1
                        slope = 1
                    else: 
                        break
            # 내리막
            else:
                # 나올 값들이 L번 이상 나와야함
                tmp = map_list[i][j]
                if (j + (L-1)) > (N-1):
                    down_check = True
                    break
                for k in range(1,L):
                    if tmp == map_list[i][j+k]:
                        continue
                    else:
                        down_check = True
                        break
                else:
                    tmp_cnt = 1
                    slope = -1
                if down_check == True:
                    break
        # 높이 차이가 2이상
        else: break
    else:
        answer += 1

# 열 탐색
for j in range(N):
    tmp = map_list[0][j]
    # slope 경사 1 -> 오르막, -1 -> 내리막
    tmp_cnt = slope =  0 
    down_check = False
    for i in range(N):
        sub = tmp - map_list[i][j]
        # 같은 값인 경우
        if sub == 0:
            tmp_cnt += 1
        elif abs(sub) < 2 :
            # 오르막
            if sub < 0:
                # 원래 내리막이었던 경우
                if slope == -1:
                    # 나왔던 값들의 개수가 L보다 커야함 (하나는 내리막용 경사)
                    if tmp_cnt >= 2 * L:
                        tmp = map_list[i][j]
                        tmp_cnt = 1
                        slope = 1
                    else: break
                # 원래 평지/오르막이었던 경우
                else:
                    if tmp_cnt >= L:
                        tmp = map_list[i][j]
                        tmp_cnt = 1
                        slope = 1
                    else: break
            # 내리막
            else:
                # 나올 값들이 L번 이상 나와야함
                tmp = map_list[i][j]
                if (i + (L-1)) > (N-1):
                    down_check = True
                    break
                for k in range(1,L):
                    if tmp == map_list[i+k][j]:
                        continue
                    else:
                        down_check = True
                        break
                else:
                    tmp_cnt = 1
                    slope = -1
                if down_check == True:
                    break
        # 높이 차이가 2이상
        else: break
    else:
        answer += 1

print(answer)