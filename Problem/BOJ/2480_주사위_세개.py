# 2480 주사위 세개

'''
시작시각 03:30
종료시각 03:33
'''

def game(num1, num2, num3):
    if num1 == num2 and num2 == num3:
        return 10000 + num1 * 1000
    elif num1 == num2 and num2 != num3:
        return 1000 + num1 * 100
    elif num1 == num3 and num1 != num2:
        return 1000 + num1 * 100
    elif num2 == num3 and num1 != num2:
        return 1000 + num2 * 100
    else:
        return max(num1, num2, num3) * 100


num1, num2, num3 = map(int, input().split())
answer = game(num1, num2, num3)

print(answer)