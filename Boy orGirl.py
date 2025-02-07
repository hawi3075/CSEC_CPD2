def determine_gender(username):
    
    distinct_characters = set(username)
    
    if len(distinct_characters) % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"


username = input().strip()


print(determine_gender(username))
