from collections import deque


def make_a_move(r, c, matrx):
    found_hazelnuts = 0
    if not (0 <= r < len(matrx) and 0 <= c <= len(matrx)):
        print("The squirrel is out of the field.")
        return
    if matrx[r][c] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        return
    if matrx[r][c] == "h":
        found_hazelnuts += 1
    matrx[r][c] = "*"
    return found_hazelnuts, matrx


matrix_size = int(input())

commands = deque(x for x in (input().split(", ")))

matrix = []
hazelnut_counter = 0
squirrel_coordinates = []
squirrel_trap = False

for row in range(matrix_size):
    current_row = (input())
    matrix.append(list(current_row))

for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == 's':
            squirrel_coordinates = [row, col]

matrix[squirrel_coordinates[0]][squirrel_coordinates[1]] = "*"
for command in commands:
    if command == "up":
        squirrel_coordinates[0] -= 1
    elif command == "down":
        squirrel_coordinates[0] += 1
    elif command == "left":
        squirrel_coordinates[1] -= 1
    elif command == "right":
        squirrel_coordinates[1] += 1
    result = make_a_move(squirrel_coordinates[0], squirrel_coordinates[1], matrix)
    if not result:
        squirrel_trap = True
        break

    count_hazelnuts, matrix = result[0], result[1]

    hazelnut_counter += count_hazelnuts
    if hazelnut_counter == 3:
        print("Good job! You have collected all hazelnuts!")
        break

if not squirrel_trap and hazelnut_counter < 3:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnut_counter}")
