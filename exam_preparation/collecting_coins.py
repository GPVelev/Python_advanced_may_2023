from math import floor


def find_player_coordinates(r, c, matrx):
    for row in range(r):
        for col in range(c):
            if matrx[row][col] == 'P':
                return [row, col]


size = int(input())
rows, cols = size, size

matrix = []

directions = {
    "left": lambda r, c: [r, (c - 1) % size],
    "right": lambda r, c: [r, (c + 1) % size],
    "up": lambda r, c: [(r - 1) % size, c],
    "down": lambda r, c: [(r + 1) % size, c],
}

for i in range(size):
    matrix.append(input().split())

player_coordinates = find_player_coordinates(rows, cols, matrix)
matrix[player_coordinates[0]][player_coordinates[1]] = 0
player_path = []
touched_walls = False
collected_coins = 0
player_path.append(player_coordinates)

while not touched_walls:
    command = input()
    if command == "left":
        player_coordinates = directions["left"](*player_coordinates)
    elif command == "right":
        player_coordinates = directions["right"](*player_coordinates)
    elif command == "up":
        player_coordinates = directions["up"](*player_coordinates)
    elif command == "down":
        player_coordinates = directions["down"](*player_coordinates)

    position = matrix[player_coordinates[0]][player_coordinates[1]]

    player_path.append(player_coordinates)
    if position == "P":
        position = 0
    if position == "X":

        touched_walls = True
        break
    else:
        collected_coins += int(position)
        position = 0

    if collected_coins >= 100:
        collected_coins = floor(collected_coins)
        break

if not touched_walls:
    print(f"You won! You've collected {collected_coins} coins.")
if touched_walls:
    collected_coins = floor(collected_coins * 0.5)
    print(f"Game over! You've collected {collected_coins} coins.")

print("Your path:")
print("\n".join(str(x) for x in player_path))
