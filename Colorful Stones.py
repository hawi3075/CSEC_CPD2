def final_position(s, t):
    position = 1  
    for instruction in t:
        if position <= len(s) and s[position - 1] == instruction:
            position += 1
    return position


s = input().strip()
t = input().strip()


print(final_position(s, t))
