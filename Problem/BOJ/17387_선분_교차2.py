# 17387 선분 교차2
# 220930

'''
시작시간 11:04
종료시간 15:15
'''

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2 + x2*y3 + x3*y1 - (x2*y1 + x3*y2 + x1*y3)


def check(ccw1, ccw2, ccw3, ccw4):
    if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:
        if max(x1, x2) < min(x3, x4):
            return 0
        if min(x1, x2) > max(x3, x4):
            return 0
        if max(y1, y2) < min(y3, y4):
            return 0
        if min(y1, y2) > max(y3, y4):
            return 0
        return 1
    
    if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
        return 1
    else:
        return 0


x1, y1, x2, y2 = list(map(int, input().split()))
x3, y3, x4, y4 = list(map(int, input().split()))

ccw123 = ccw(x1, y1, x2, y2, x3, y3)
ccw124 = ccw(x1, y1, x2, y2, x4, y4)

ccw341 = ccw(x3, y3, x4, y4, x1, y1)
ccw342 = ccw(x3, y3, x4, y4, x2, y2)

answer = check(ccw123, ccw124, ccw341, ccw342)
print(answer)