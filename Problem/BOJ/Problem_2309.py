import itertools

height =  []   # 9명의 키를 list에 저장
for _ in range(9):
    height.append(int(input()))

for comb in itertools.combinations(height, 7):  # 9명 중 7명의 키 값을 불러옴
    if sum(comb) == 100:  # 합이 100이면 정렬 후 하나씩 출력
        for i in sorted(comb):
            print(i)
        break