N = int(input())

def Hanoi_cnt(N):
    if N == 1:
        return 1
    return Hanoi_cnt(N-1) + 1 + Hanoi_cnt(N-1)

print(Hanoi_cnt(N))

def Hanoi(N, s, e):
    if N == 1:
        return (f'{s} {e}\n')
    if s == 1 :
        if e == 3:
            return (Hanoi(N-1, 1, 2)) + (f'{s} {e}\n') + (Hanoi(N-1, 2, 3))
        elif e == 2:
            return (Hanoi(N-1, 1, 3)) + (f'{s} {e}\n') + (Hanoi(N-1, 3, 2))
    elif s == 2:
        if e == 3:
            return (Hanoi(N-1, 2, 1)) + (f'{s} {e}\n') + (Hanoi(N-1, 1, 3))
        elif e == 1:
            return (Hanoi(N-1, 2, 3)) + (f'{s} {e}\n') + (Hanoi(N-1, 3, 1))
    elif s == 3:
        if e == 1:
            return (Hanoi(N-1, 3, 2)) + (f'{s} {e}\n') + (Hanoi(N-1, 2, 1))
        elif e == 2:
            return (Hanoi(N-1, 3, 1)) + (f'{s} {e}\n') + (Hanoi(N-1, 1, 2))

print(Hanoi(N, 1, 3))