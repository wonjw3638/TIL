N = int(input())
S = input()
tmp = S[0]
cnt = 1

for char in S:
	if char == tmp:
		continue
	else:
		cnt += 1
		tmp = char

print(cnt)
