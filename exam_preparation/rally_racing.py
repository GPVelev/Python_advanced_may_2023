def find_exit_tunnel(mtrx):
    for row in range(len(mtrx)):
        for col in range(len(mtrx[row])):
            if mtrx[row][col] == "T":
                return row, col


size = int(input())
racing_number = int(input())

matrix = []
total_km = 0
car_coordinates = [0, 0]
for _ in range(size):
    matrix.append(input().split())

while True:
    command = input()
    if command == "End":
        matrix[car_coordinates[0]][car_coordinates[1]] = "C"
        print(f"Racing car {racing_number} DNF.")
        break
    elif command == "left":
        car_coordinates[1] -= 1
    elif command == "right":
        car_coordinates[1] += 1
    elif command == "down":
        car_coordinates[0] += 1
    elif command == "up":
        car_coordinates[0] -= 1

    if matrix[car_coordinates[0]][car_coordinates[1]] == "F":
        total_km += 10
        matrix[car_coordinates[0]][car_coordinates[1]] = "C"
        print(f"Racing car {racing_number} finished the stage!")
        break
    elif matrix[car_coordinates[0]][car_coordinates[1]] == "T":
        total_km += 30
        matrix[car_coordinates[0]][car_coordinates[1]] = "."
        car_coordinates[0], car_coordinates[1] = find_exit_tunnel(matrix)
        matrix[car_coordinates[0]][car_coordinates[1]] = "."
    else:
        total_km += 10

print(f"Distance covered {total_km} km.")
for row in range(len(matrix)):
    print("".join(matrix[row]))
