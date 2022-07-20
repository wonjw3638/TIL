dice = { 0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0 } # 아랫면 선택시 와야하는 윗면 idx
N = int(input()) # 주사위 개수
temp = 0
first = input().split()
now_idx , nex_idx , value = 0, 0, 0 # 현재 idx, 다음 idx, 맞닿는 주사위 값

def max_val(now_idx, nex_idx, dice_val):
    now = dice_val[now_idx]  #now, nex idx 제외, 최댓값 구하기
    nex = dice_val[nex_idx]
    dice_val[now_idx] = 0
    dice_val[nex_idx] = 0
    max_value = max(dice_val) 
    dice_val[now_idx] = now
    dice_val[nex_idx] = nex 
    return max_value

for i in range(1,7):
    ans = 0
    value = i
    now_idx = first.index(value)
    nex_idx = dice[int(now_idx)]
    value = first[nex_idx]
    ans += max_val(now_idx, nex_idx, first)
    for num in range(N-1):
        dices = input().split()
        now_idx = dices.index(value)
        nex_idx = dice[int(now_idx)]
        value = dices[nex_idx]
        ans += max_val(now_idx, nex_idx, dices)
    if ans > temp:
        ans = temp

print(ans)


########## 아직 푸는 중 ########## 