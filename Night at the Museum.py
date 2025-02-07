def calculate_rotations(name):
    current_position = 'a'
    total_rotations = 0

    for char in name:
        distance = abs(ord(char) - ord(current_position))
        rotations = min(distance, 26 - distance)
        total_rotations += rotations
        current_position = char

    return total_rotations


name = input().strip()


print(calculate_rotations(name))
