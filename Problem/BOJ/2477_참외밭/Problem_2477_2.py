# 런타임 에러

N = int(input()) # 참외의 개수
defense = {
    '423131' : [(3, 4), (0, 1)],
    '421313' : [(4, 5), (1, 2)],
    '424231' : [(1, 2), (4, 5)],
    '423231' : [(2, 3), (0, 5)],
}

shape = ''
length = []

for _ in range(6):
    edge = input().split()
    shape += edge[0]
    length.append(int(edge[1]))

key = ''
idx = 0

for i in range(6):
    if ( shape[i:6-0] + shape[:i] ) in defense.keys():
        key = ( shape[i:6-0] + shape[:i] )
        idx = i
    else:
        continue

#############idx 범위 넘어가는거 생각하기

print(f'length : {length}')
print(f'idx : {idx}')
print(f'key : {key}')
print( f'점검용 : {(defense[key])[1][0] + idx}' )

total_area = length[ ((defense[key])[1][0] + idx) % 6 ] * length[ ((defense[key])[1][1] + idx) % 6 ]
except_area = length[ ((defense[key])[0][0] + idx) % 6 ] * length[ ((defense[key])[0][1] + idx) % 6 ]

print( N * (total_area - except_area) )