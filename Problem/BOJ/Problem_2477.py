# 런타임 에러

N = int(input())
defense = { 1 : 4, 2 : 3, 3 : 1, 4 : 2 }
area = { i : 0 for i in [1, 2, 3, 4]}

field = []
for _ in range(6):
    field.append(list(map(int, input().split())))

temp = field[0][0]
except_area = []
total_area = []
idx = []

for i in field:
    area[i[0]] += 1
    if i[0] == temp:
        temp = defense[i[0]]
        continue
    else:
        idx.append(field.index(i) - 1)

for i in range(1,5):
    if area[i] == 1:
        for f in field:
            if f[0] == i:
                total_area.append(f[1])

for i in idx:
    except_area.append(field[i][1])

print((N * ((total_area[0] * total_area[1]) - (except_area[0] * except_area[1]))))