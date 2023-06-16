MATRIX_SIZE = 6

first_player, second_player = input().split(", ")

first_player_needs_rest = False
second_player_needs_rest = False


matrix = []

for _ in range(MATRIX_SIZE):
    matrix.append(input().split())


while True:

    coordinates = input()
    if not first_player_needs_rest:
        row, col = map(int, coordinates.strip("(").strip(")").split(", "))
        player_coordinates = matrix[row][col]
        if player_coordinates == "E":
            print(f"{first_player} found the Exit and wins the game!")
            break
        if player_coordinates == "T":
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break
        if player_coordinates == "W":
            print(f"{first_player} hits a wall and needs to rest.")
            first_player_needs_rest = True
    else:
        first_player_needs_rest = False

    coordinates = input()
    if not second_player_needs_rest:
        row, col = map(int, coordinates.strip("(").strip(")").split(", "))
        player_coordinates = matrix[row][col]
        if player_coordinates == "E":
            print(f"{second_player} found the Exit and wins the game!")
            break
        if player_coordinates == "T":
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break
        if player_coordinates == "W":
            print(f"{second_player} hits a wall and needs to rest.")
            second_player_needs_rest = True
    else:
        second_player_needs_rest = False
