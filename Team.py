def count_solutions(n, problems):
    count = 0
    for problem in problems:
        if sum(problem) >= 2:
            count += 1
    return count

# Read input
n = int(input())
problems = [list(map(int, input().split())) for _ in range(n)]


print(count_solutions(n, problems))
