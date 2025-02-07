def find_one(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                return (i, j)

def moves_to_center(matrix):
    x, y = find_one(matrix)
    return abs(x - 2) + abs(y - 2)


matrix = []
for _ in range(5):
    matrix.append(list(map(int, input().split())))


print(moves_to_center(matrix))
