T = int(input()) # Test case개수 입력 받음

for case in range(1, T+1):
    string = input() # 문자열 입력
    r_string = string[::-1]  # 문자열 역순로 변수  저장
    if string == r_string:  # 문자열과 역순이 같다면 1출력, 아니면 0출력
        print(f'#{case} 1')
    else: print(f'#{case} 0')