# 1958 LCS3
# 221010

mainString = '0' + input()
subString = '0' + input()
thirdString = '0' + input()

# 첫 행과 열은 비워두기, 3차원 배열 만들기
dpLen = [[[0] * (len(thirdString)) for _ in range(len(subString))] for _ in range(len(mainString))]

for i in range(1, len(mainString)):
    for j in range(1, len(subString)):
        for k in range(1, len(thirdString)):
            # 비교한 문자열이 같으면 왼쪽 위의 값에서 += 1
            if mainString[i] == subString[j] and subString[j] == thirdString[k]:
                dpLen[i][j][k] = dpLen[i-1][j-1][k-1] + 1

            # 위랑 왼쪽중에 큰 값
            else:
                dpLen[i][j][k] = max(dpLen[i][j][k-1], dpLen[i][j-1][k], dpLen[i-1][j][k])

print(dpLen[-1][-1][-1])