# 2407 조합
# 220923

'''
설계시간  
구현시간 17:02~17:03
'''

n, c = list(map(int, input().split()))

tmp1 = tmp2 = 1

for i in range(c):
    tmp1 = tmp1 * (n - i)

for i in range(1, c+1):
    tmp2 = tmp2 * i

answer = tmp1//tmp2
print(answer)
