def bird_shooting(n, birds, shots):
    for x, y in shots:
        x -= 1  
        if x > 0:
            birds[x - 1] += y - 1  
        if x < n - 1:
            birds[x + 1] += birds[x] - y  
        birds[x] = 
    return birds


n = int(input())
birds = list(map(int, input().split()))
m = int(input())
shots = [tuple(map(int, input().split())) for _ in range(m)]


result = bird_shooting(n, birds, shots)
for count in result:
    print(count)
