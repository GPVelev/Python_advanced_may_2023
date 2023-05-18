number_of_rows = int(input())
matrix = []
for row in range(number_of_rows):
    row_data = list(map(int, input().split(', ')))
    matrix.append(row_data)
result = [num for row in matrix for num in row]
print(result)