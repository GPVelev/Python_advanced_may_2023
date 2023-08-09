


rows, cols = map(int, input().split())
matrix = [list(input()) for _ in range(rows)]
boy_coordinates = None
boy_coordinates_copy = boy_coordinates

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == 'B':
            boy_coordinates = (r, c)
            boy_coordinates_copy = boy_coordinates
            break

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

while True:
    command = input().strip()
    if command == "up" or command == "down" or command == "right" or command == "left":
        dir_r, dir_c = directions[command]
        new_row, new_col = boy_coordinates[0] + dir_r, boy_coordinates[1] + dir_c

        if 0 <= new_row < rows and 0 <= new_col < cols:
            if matrix[new_row][new_col] == '*':
                continue

            elif matrix[new_row][new_col] == 'A':
                matrix[new_row][new_col] = 'P'
                print("Pizza is delivered on time! Next order...")
                break

            elif matrix[new_row][new_col] == 'P':
                matrix[new_row][new_col] = 'R'
                print("Pizza is collected. 10 minutes for delivery.")
            elif matrix[new_row][new_col] == '-':
                matrix[new_row][new_col] = '.'

            boy_coordinates = (new_row, new_col)
        else:
            print("The delivery is late. Order is canceled.")
            matrix[boy_coordinates_copy[0]][boy_coordinates_copy[1]] = ' '
            break
for row in matrix:
    print(''.join(row))