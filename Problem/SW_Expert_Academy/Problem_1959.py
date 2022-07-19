T = int(input())
for case in range(T):
    N, M = map(int, input().split())
    if N < M:
        sht = list((input().split()))
        lng = list(input().split())
    else : 
        lng = list((input().split()))
        sht = list((input().split()))
    ran, ans = 0, 0
    while ran+len(sht) <= len(lng):
        temp = 0
        for idx in range(0,len(sht)):
            temp += int(sht[idx])*int(lng[ran+idx])
        ran += 1
        if temp > ans: ans = temp
    print(f'#{case+1} {ans}')