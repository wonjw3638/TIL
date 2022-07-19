N = int(input())
num = list(input().split())
num.sort(key=int)
print(num[N//2])