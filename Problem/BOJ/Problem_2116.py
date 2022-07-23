dice_num = { 0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0 } # 아랫면 선택시 와야하는 윗면 idx
N = int(input()) # 주사위 개수
dice_list = []  # 주사위 값 입력, 저장
now_idx , nex_idx , value = 0, 0, 0 # 현재 idx, 다음 idx, 맞닿는 주사위 값
max_sum = 0   # 현재 단계까지 합의 최대값

for _ in range(N):
    dice_list.append(list(map(int, input().split())))

def max_val(now_idx, nex_idx, dice_val):  # 주사위에서 가장 큰 면의 값 구하기

    now = dice_val[now_idx]  # now, nex idx 제외, 최댓값 구하기
    nex = dice_val[nex_idx]
    dice_val[now_idx], dice_val[nex_idx] = 0, 0
    max_value = max(dice_val) 

    dice_val[now_idx] = now  # 최댓값 구한 후 제외한 now, nex idx 해당하는 값 복구
    dice_val[nex_idx] = nex 
    return max_value

for first_value in range(1,7):  # 첫번째 주사위 아랫면 값 택1 ( 1~6)
    ans = 0 # 모든 주사위 가장 큰 면의 합
    value = first_value

    for dice in dice_list:  # 모든 주사위에 대한 최댓값 탐색
        now_idx = dice.index(value)  # 현재 해당 면에 대한 주사위 idx 값 찾기
        nex_idx = dice_num.get(now_idx)  # 해당 idx 값에 따른 다음 면의 idx값 찾기
        ans += max_val(now_idx, nex_idx, dice) # 위, 아랫 면 값을 제외한 면 중에 최댓값 찾아 더하기
        value = dice[nex_idx]  # 바뀌는 면의 값 찾아서 다음 주사위로 넘어감

    if ans > max_sum: 
        max_sum = ans  # 모든 주사위 탐색후 합한 값이 전보다 크면 값 덮어쓰기

print(max_sum)