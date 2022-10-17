# 1.

```python
N = int(input())
arr = list(map(int, input().split()))
answer = 1
for idx in range(N):
	answer *= arr[idx]
print (answer)
```

<br>

# 2.

```python
n, name = list(input().split())
answer = 0
for _ in range(int(n)):
	string = input()
	if name in string:
		answer += 1
print(answer)
```

<br>

# 3.

```python
a, b, c, d = list(map(int, input().split()))
answer1 = abs(a - b) + abs(c - d)
answer2 = abs(a - c) + abs(b - d)
answer3 = abs(a - d) + abs(b - c)
print(max(answer1, answer2, answer3))
```

<br>

# 4.

```python
a, b, c, d = list(map(int, input().split()))
answer1 = abs(a - b) + abs(c - d)
answer2 = abs(a - c) + abs(b - d)
answer3 = abs(a - d) + abs(b - c)
print(max(answer1, answer2, answer3))
```

