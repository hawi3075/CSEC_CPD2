def count_guest_uniform_games(n, teams):
    guest_uniform_games = 0
    
    for i in range(n):
        for j in range(n):
            if i != j and teams[i][0] == teams[j][1]:
                guest_uniform_games += 1
                
    return guest_uniform_games


n = int(input())
teams = [tuple(map(int, input().split())) for _ in range(n)]


print(count_guest_uniform_games(n, teams))
