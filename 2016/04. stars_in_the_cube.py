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
            cube[y].append(input_data[y].split())

    return cube

def add_star_to_dict(el, stars):

    if not el in stars:
        stars[el] = 0

    stars[el] += 1


def get_total_number_stars(stars):
    result = 0

    for value in stars.values():
        result += value

    return result


def print_result(stars):

    if not stars:
        total_stars = 0
        print(f"{total_stars}")

    else:
        total_stars = get_total_number_stars(stars)
        print(f"{total_stars}")
        print('\n'.join(f"{key} -> {value}" for key, value in dict(sorted(stars.items())).items()))


size = int(input())
cube = create_cube(size)
stars = {}

for x in range(1, size - 1):
    for y in range(1, size - 1):
        for z in range(1, size -1):
            el = cube[x][y][z]
            star_counter = 1

            for delta in deltas:
                next_x = x + delta[0]
                next_y = y + delta[1]
                next_z = z + delta[2]

                if not cube[next_x][next_y][next_z] == el:
                    break

                star_counter += 1

            if star_counter == 7:
                add_star_to_dict(el, stars)

print_result(stars)