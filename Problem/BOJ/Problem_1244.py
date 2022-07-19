switch_cnt = int(input()) # 스위치 개수 입력
switch = input().split() # 스위치 상태 입력, list형 저장
students = int(input()) # 학생 수

light = { '0' : '1', '1' : '0'} # 스위치 on off dictionary 생성

def turn(switch, idx): # 스위치 1 -> 0, 0 -> 1
    switch[idx] = light[switch[idx]]

def boy(switch, num, n): # 남자인 경우 배수인 switch 변환
    rng = n//num
    for idx in range(1, rng+1):
        turn(switch, (idx*num)-1) # list idx는 0부터 시작함에 주의
    return switch

def girl(switch, num, n): # 여자인 경우 최대 대칭일 때 switch 변환
    sym = True
    rng = 0
    while sym == True : # sym 변수 선언, 최대로 좌우 대칭일 때까지 반복, 범위 찾기 
        if (num-1)-rng >= 0 and (num-1)+rng < n:
            if switch[(num-1)-rng] == switch[(num-1)+rng]:
                rng += 1
            else: 
                sym = False #대칭 아닌 부분 나오면 전까지만 rng값 보정
                rng -= 1
        else: 
            rng -= 1
            break #범위 벗어나면 중단
    for idx in range(num-1-rng, num+rng): 
        turn(switch, idx) # 범위에서 0부터 시작인거 고려해줬으니까 그대로
    return switch 

for i in range(students) : # 학생 수 만큼 for문 돌리기
    gender, num = map(int, input().split()) # 학생의 성별은 gender, 받은 번호는 num에 저장
    if gender == 1:
        boy(switch, num, switch_cnt) # 학생이 남자인 경우
    else: 
        girl(switch, num, switch_cnt) # 학생이 여자인 경우

cnt = 0
while cnt <= switch_cnt: # 20개씩 출력
    temp = switch[0+cnt:20+cnt]
    answer = ' '.join(i for i in temp)
    print(answer)
    cnt += 20