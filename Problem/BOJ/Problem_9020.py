import math

N = int(input())

def Goldbach(num):
    for i in range(num // 2):
        if (prime((num // 2) - i) and prime((num // 2) + i)):
            return print(((num // 2) - i), ((num // 2) + i))
        else:
            continue

def prime(num):
    for n in range(2, int((math.sqrt(num) + 1))):
        if num % n == 0: return False
    else: return True
        
for _ in range(N):
    number = int(input())
    Goldbach(number)