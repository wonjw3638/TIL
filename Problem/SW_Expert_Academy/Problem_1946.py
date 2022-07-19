T = int(input())
for case in range(1,T+1):
    print(f"#{case}")
    n = int(input())
    ans = ""
    for i in range(n):
        Ci, Ki = map(str, input().split())
        ans += Ci*int(Ki)
    rge = 0
    while rge <= len(ans):
        print(ans[0+rge:10+rge])
        rge += 10