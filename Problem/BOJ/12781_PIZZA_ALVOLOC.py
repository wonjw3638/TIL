# 12781 PIZZA ZLVOLOC
# 220920

def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

x1, y1, x2, y2, x3, y3, x4, y4 = list(map(int, input().split()))

ccw123 = ccw(x1, y1, x2, y2, x3, y3)
ccw124 = ccw(x1, y1, x2, y2, x4, y4)

if x1 == x2 and (x1 == x3 or x1 == x4):
    print(0)
if x3 == x4 and (x3 == x1 or x2 == x2):
    print(0)
if y1 == y2 and (y1 == y3 or y1 == y4):
    print(0)
if x3 == x4 and (x3 == x1 or x2 == x2):
    print(0)

if ccw123 * ccw124 <= 0:
    print(1)
else:
    print(0)


