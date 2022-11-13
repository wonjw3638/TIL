for _ in range(5):
    arr = list(map(int, list(input())))
    
    a = 0
    for idx in [0, 2, 4, 6]:
        a += arr[idx]
    
    for idx in [1, 3, 5]:
        if arr[idx] == 0:
            continue
        a *= arr[idx]
    
    print(a%10)