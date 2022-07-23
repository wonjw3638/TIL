N = int(input())  # 기둥의 개수
col_list = [] # 기둥의 위치, 높이 값을 저장할 리스트 
for _ in range(N) :
    col_list.append(list(map(int, input().split())))
    
max_l = max(loc[0] for loc in col_list)  # 가장 마지막에 있는 기둥의 위치
max_h = max(hei[1] for hei in col_list)  # 가장 큰 기둥의 높이
area = [0 for _ in range(max_l + 1)]  # 가장 마지막 기둥까지 0으로 채운 리스트 작성 [0, 0, ... , 0]

for col in col_list :       # 기둥위치 index에 높이 값을 가지는 list작성
    area[(col[0])] = col[1]

left_h, idx = 0, 0
while True :   # 왼쪽에서부터 만난 더 큰 기둥값으로 바꿔줌
    if area[idx] == max_h : break  # 가장 큰 기둥을 만나면 반복문 탈출
    if area[idx] > left_h :
        left_h = area[idx]
    else: area[idx] = left_h
    idx += 1

right_h, idx = 0, max_l
while True :   # 오른쪽에서부터 만난 더 큰 기둥값으로 바꿔줌
    if area[idx] == max_h : break  # 가장 큰 기둥을 만나면 반복문 탈출
    if area[idx] > right_h :
        right_h = area[idx]
    else: area[idx] = right_h
    idx -= 1

# 가장 큰 기둥이 여러개인 경우 고려하기
max_list = []
for max_col in col_list :
    if max_col[1] == max_h : 
        max_list.append(max_col[0])

for max_idx in range(min(max_list), max(max_list)+1):   # idx가 가장 작은 기둥~ 큰 기둥까지 가장 큰 기둥의 높이 값으로 바꿔줌
    area[max_idx] = max_h

print(sum(area))