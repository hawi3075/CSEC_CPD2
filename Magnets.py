def count_magnet_groups(n, magnets):
    groups = 1  
    for i in range(1, n):
        if magnets[i] != magnets[i - 1]:
            groups += 1
    return groups


n = int(input())
magnets = [input().strip() for _ in range(n)]


print(count_magnet_groups(n, magnets))
