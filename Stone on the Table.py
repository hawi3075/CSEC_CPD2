def count_removals(s):
    removals = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            removals += 1
    return removals


n = int(input())
s = input().strip()


print(count_removals(s))
