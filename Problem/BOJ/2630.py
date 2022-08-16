N = int(input())

confetti = []  #색종이
white , blue = 0, 0

for i in range(N):
    color = list(map(int, input().split()))
    confetti.append(color)

def Cut(x, y, N):
    global white, blue

    if N == 1:
        if confetti[x][y] == 1: 
            blue += 1
            return None
        else: 
            white += 1
            return None
    else:
        tmp = confetti[x][y]
        brk = False
        for i in range(x, x+N):
            if brk == True:
                break
            for j in range(y, y+N):
<<<<<<< HEAD
                if confetti[i][j] == tmp: continue
                else: 
                    brk = True
                    break
        else:
=======
                if confetti[i][j] == tmp:
                    continue
                else: 
                    brk = True
                    break
        
        if brk == False:
>>>>>>> 64db1712e18fff3c64a326fc095db4ca23f69315
            if tmp == 1: 
                blue += 1 
                return None
            else: 
                white += 1
                return None
<<<<<<< HEAD

        Cut(x, y, N//2)
        Cut(x, y+N//2, N//2)
        Cut(x+N//2, y, N//2)
        Cut(x+N//2, y+N//2, N//2)
=======
        else:
            Cut(x, y, N//2)
            Cut(x, y+N//2, N//2)
            Cut(x+N//2, y, N//2)
            Cut(x+N//2, y+N//2, N//2)
>>>>>>> 64db1712e18fff3c64a326fc095db4ca23f69315

        return None

Cut(0, 0, N)

print(white)
print(blue)