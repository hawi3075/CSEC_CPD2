def calculate_calories(a, s):
    total_calories = 0
    for char in s:
        total_calories += a[int(char) - 1]
    return total_calories


a = list(map(int, input().split()))
s = input().strip()


print(calculate_calories(a, s))
