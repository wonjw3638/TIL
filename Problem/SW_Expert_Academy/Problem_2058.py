rem = int(input())
ans = 0
while rem>0:
    ans += rem%10
    rem = rem//10
print(ans)