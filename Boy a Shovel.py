def find_min_shovels(k, r):
    for i in range(1, 11):
        total_cost = k * i
        if total_cost % 10 == 0 or total_cost % 10 == r:
            return i

# Read input
k, r = map(int, input().split())

# Output the result
print(find_min_shovels(k, r))
