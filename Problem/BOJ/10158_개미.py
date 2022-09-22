import sys
input = sys.stdin.readline

w, h = list(map(int, input().split()))
p, q = list(map(int, input().split()))
T = int(input())

pt = T % (2 * w)
qt = T % (2 * h)

a =  1
for _ in range(pt):
    np = p + a
    if  np > w:
        a = -1
        p += a
    elif np < 0:
        a = 1
        p += a
    else:
        p += a

a =  1
for _ in range(qt):
    nq = q + a
    if  nq > h:
        a = -1
        q += a
    elif nq < 0:
        a = 1
        q += a
    else:
        q += a

print(p, q)