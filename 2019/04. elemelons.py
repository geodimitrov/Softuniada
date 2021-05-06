dimensions = [
    (0, -1, 0), (0, 0, +1),
    (0, +1, 0), (0, 0, -1),
    (+1, 0, 0), (-1, 0, 0)
]

def create_3D_matrix(size):
    result = []

    for x in range(size):
        line = input().split(" | ")
        result.append([el.split() for el in line])

    return result


def change_cell_value_to_harvested(matrix, row, layer, col):
    matrix[row][layer][col] = "0"


def get_cells_in_direct_sight(row, layer, col):
    result = []

    for d in dimensions:
        next_row = row + d[0]
        next_layer = layer + d[1]
        next_col = col + d[2]

        result.append((next_row, next_layer, next_col))

    return result

def harvest_melons(matrix, end):

    while True:
        command = input()

        if command == end:
            break

        layer, row, col = map(int, command.split())
        change_cell_value_to_harvested(matrix, row, layer, col)
        cells_in_direct_sight = get_cells_in_direct_sight(row, layer, col)

        for row in range(size):
            for layer in range(size):
                for col in range(size):
                    if (row, layer, col) not in cells_in_direct_sight:
                        element = matrix[row][layer][col]

                        if element == "W":
                            matrix[row][layer][col] = "E"

                        elif element == "E":
                            matrix[row][layer][col] = "F"
                        elif element == "F":
                            matrix[row][layer][col] = "A"
                        elif element == "A":
                            matrix[row][layer][col] = "W"


def print_result(matrix):
    for row in matrix:
        print(" | ".join(' '.join(el) for el in row))


end_command = "Melolemonmelon"
size = int(input())
matrix = create_3D_matrix(size)
harvest_melons(matrix, end_command)
print_result(matrix)