def gravity_flip(n, columns):
    
    columns.sort()
    return columns


n = int(input())
columns = list(map(int, input().split()))


result = gravity_flip(n, columns)


print(" ".join(map(str, result)))
