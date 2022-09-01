maplist = [[0] * 100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = list(map(int, input().split()))
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            maplist[i][j] += 1

area = 0

for i in range(100):
    for j in range(100):
        if maplist[i][j] > 0:
            area += 1
        
print(area)