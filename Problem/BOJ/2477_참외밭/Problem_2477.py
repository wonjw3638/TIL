# 2477_참외밭
# 220816
# 설계 13:30 ~ 13:35
# 구현 13:35 ~ 

K = int(input())

# 같은 방향에 둘러싸인 값 반환
# 한번만 나온 방향 값 -> 진짜 크기

edge = list()
length = list()
count = [0] * 5

for _ in range(6):
    E, L = list(map(int, input().split()))
    edge.append(E)
    length.append(L)
    count[E] += 1

width = height = except_w = except_h = 0

print('count:', count)

for i in range(6):
    if count[edge[i]] == 1:
        if edge[i] in [1, 2]:
            width = length[i]
        else:
            height = length[i]
    if i == 5:
        if edge[i-1] == edge[0]:
            if edge[i] in [1, 2]:
                except_w = length[i]
            else:
                except_h = length[i]
        continue
    
    if edge[i-1] == edge[i+1]:
        if edge[i] in [1, 2]:
            except_w = length[i]
        else:
            except_h = length[i]

print('width', width)
print('height', height)
print('except_w', except_w)
print('except_h', except_h)


answer = K * ((width * height)-(except_w * except_h))
print(answer)

'''
7
3 20
1 100
4 50
2 160
3 30
1 60
'''