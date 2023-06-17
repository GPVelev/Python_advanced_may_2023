
rows, cols = map(int, input().split(","))

matrix = []
mouse_coordinates = [0, 0]
cheese_counter = 0
cheese_in_matrix = 0

for row in range(rows):
    current_row = input()
    current_row_matrix = []
    for el in current_row:
        if "C" == el:
            cheese_in_matrix += 1
        if "M" == el:
            mouse_coordinates = [row, current_row.index(el)]
        current_row = [el for el in current_row]
    matrix.append(current_row)



try:
    while True:
        matrix[mouse_coordinates[0]][mouse_coordinates[1]] = "*"
        command = input()
        if command == "danger":
            print("Mouse will come back later!")
            break
        elif command == "left":
            mouse_coordinates[1] -= 1
        elif command == "right":
            mouse_coordinates[1] += 1
        elif command == "down":
            mouse_coordinates[0] += 1
        elif command == "up":
            mouse_coordinates[0] -= 1
        if matrix[mouse_coordinates[0]][mouse_coordinates[1]] == "C":
            matrix[mouse_coordinates[0]][mouse_coordinates[1]] = "M"
            cheese_counter += 1
            if cheese_counter == cheese_in_matrix:
                print(f"Happy mouse! All the cheese is eaten, good night!")
                break
        elif matrix[mouse_coordinates[0]][mouse_coordinates[1]] == "*":
            matrix[mouse_coordinates[0]][mouse_coordinates[1]] = "M"
            continue
        elif matrix[mouse_coordinates[0]][mouse_coordinates[1]] == "@":
            continue
        elif matrix[mouse_coordinates[0]][mouse_coordinates[1]] == "T":
            matrix[mouse_coordinates[0]][mouse_coordinates[1]] = "M"
            print("Mouse is trapped!")
            break

except IndexError:
    print("No more cheese for tonight!")

for row in range(len(matrix)):
    print("".join(matrix[row]))
