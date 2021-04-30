# cube_data = [[
#         [1, 2, 4],
#         [4, 6, 7],
#         [8, 9, 4]
#     ],
#     [
#         [6, 7, 8],
#         [4, 9, 3],
#         [4, 2, 4]
#     ],
#     [
#         [1, 1, 4],
#         [4, 4, 4],
#         [7, 9, 4]
#     ]]

deltas = [
    (0, -1, 0), (0, 0, +1),
    (0, +1, 0), (0, 0, -1),
    (+1, 0, 0), (-1, 0, 0)
]


def create_cube(size):
    cube = [[] for _ in range(size)]

    for x in range(size):
        input_data = input().split(" | ")
        for y in range(size):
            cube[y].append(list(map(int, input_data[y].split())))

    return cube


def get_wrong_value(cube, coordinates):
    x, y, z = coordinates
    return cube[x][y][z]


def in_range(size, x, y, z):
    return x in range(size) and y in range(size) and z in range(size)

def get_new_value_data(cube, deltas, x, y, z):
    new_value = 0

    for delta in deltas:
        new_x = x + delta[0]
        new_y = y + delta[1]
        new_z = z + delta[2]

        if in_range(cube_size, new_x, new_y, new_z):
            value = cube[new_x][new_y][new_z]

            if not value == wrong_value:
                new_value += value

    return (x, y, z, new_value)


def get_correct_values_data(size, cube, deltas, wrong_value):
    new_values_data = []

    for x in range(size):
        for y in range(size):
            for z in range(size):

                if cube[x][y][z] == wrong_value:
                    new_values_data.append(get_new_value_data(cube, deltas, x, y, z))

    return new_values_data


def replace_wrong_with_correct_values(cube, coordinates):
    for el in coordinates:
        x, y, z, value = el
        cube[x][y][z] = value


def get_wrong_values_count(values_data):
    return len(values_data)


def print_result(cube, size, wrong_values_count):
    print(f"Wrong values found and replaced: {wrong_values_count}")
    for x in range(size):
        for y in range(size):
            print(" ".join(list(map(str, cube[x][y]))))


cube_size = int(input())
cube = create_cube(cube_size)
wrong_value_coordinates = tuple(map(int, input().split()))

wrong_value = get_wrong_value(cube, wrong_value_coordinates)
correct_values_data = get_correct_values_data(cube_size, cube, deltas, wrong_value)
replace_wrong_with_correct_values(cube, correct_values_data)
wrong_values_count = get_wrong_values_count(correct_values_data)
print_result(cube, cube_size, wrong_values_count)
