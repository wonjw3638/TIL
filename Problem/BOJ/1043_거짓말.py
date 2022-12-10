# 1043 거짓말
# 221209

'''
시작시각 01:22
종료시각 02:00
'''

import sys
input = sys.stdin.readline

# 사람의 수 N, 파티의 수 M
N, M = map(int, input().split())
# 진실을 아는 사람의 수, 번호
trueInput = list(map(int, input().split()))

# 진실을 아는 사람은 True
true = [False] * (N + 1)
for trueIdx in trueInput[1:]:
    true[trueIdx] = True

# 같은 소식을 듣는지 판단
people = [ n for n in range(N+1) ]

# 과장된 이야기를 할 수 있는 파티 개수
partyCnt = [0] * (M)
answer = 0

# union - find 구현
def find(x):
    if people[x] != x:
        return find(people[x])
    return x

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        people[y] = x
    else:
        people[x] = y
    
    # 합치는 과정에서 둘 중 한명만 진실을 알고 있으면 둘다 알고 있는 것으로 변경
    if (true[x] == True) and (true[y] == False):
        true[y] = True
    if (true[x] == False) and (true[y] == True):
        true[x] = True


# 반복문을 돌면서, 같은 파티에 참여하는지 union-find
for m in range(M):
    party = list(map(int, input().split()))
    # 파티에 참여한 사람이 한명인 경우
    if party[0] == 1:
        find(party[1])
    # 파티에 참여한 사람이 여러명인 경우
    else:
        for idx in range(1, party[0]):
            union(party[idx], party[idx+1])
    
    partyCnt[m] = find(party[1])

# 과장되게 말할 수 있는 파티인지 확인
for m in range(M):
    ans = find(partyCnt[m])
    # 해당 파티의 parent값이 진실을 모르면 파티개수 +1
    if true[ans] == False:
        answer += 1

print(answer)