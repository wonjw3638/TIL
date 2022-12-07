# 18879 좌표압축
# 221204

'''
시작시각 02:07
종료시각 02:14
'''

# 전체 좌표개수 N
N = int(input())
# 좌표 리스트
Xarr = list(map(int, input().split()))
# 정렬된 좌표, 중복제거
Xsort = list(sorted(set(Xarr)))
# 정답을 저장할 list
answer = list()
# 압축된 좌표값을 저장할 dictionary
Xdic = dict()

# 반복문 돌면서 압축된 좌표값을 dictionary에 저장
for idx, x in enumerate(Xsort):
    Xdic[x] = idx

# 반복문을 돌면서 정렬된 index값을 추가
for x in Xarr:
    answer.append(Xdic.get(x))

print(*answer)