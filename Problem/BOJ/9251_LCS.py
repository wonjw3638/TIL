# 9251 LCS
# 221012

mainString = '0' + input()
subString = '0' + input()

# 첫 행과 열은 비워두기
dpLen = [[0] * (len(mainString)) for _ in range((len(subString)))]

for i in range(1, len(subString)):
    for j in range(1, len(mainString)):

        # 비교한 문자열이 같으면 왼쪽 위의 값에서 += 1
        if subString[i] == mainString[j]:
            dpLen[i][j] = dpLen[i-1][j-1] + 1
        # 위랑 왼쪽중에 큰 값
        else:
            if dpLen[i-1][j] < dpLen[i][j-1]:
                dpLen[i][j] = dpLen[i][j-1]
            else:
                dpLen[i][j] = dpLen[i-1][j]

print(dpLen[-1][-1])