def create_cube(size):
    result = []

    for x in range(size):
        line = input().split(" | ")
        result.append([list(el) for el in line])

    return result


def read_commands():
    result = []

    while True:

        command = input()

        if command.startswith("end"):
            result.append(command)
            break

        result.append(command)

    return result

def get_snakes_position(cube, size):
    for x in range(size):
        for y in range(size):
            for z in range(size):
                if cube[x][y][z] == "s":
                    return x, y, z


def get_next_move_dimensions(direction):
    res = None

    if direction == "up":
        res = (0, -1, 0)

    elif direction == "down":
        res = (0, +1, 0)

    elif direction == "forward":
        res = (-1, 0, 0)

    elif direction == "backward":
        res = (+1, 0, 0)

    elif direction == "right":
        res = (0, 0, +1)

    elif direction == "left":
        res = (0, 0, -1)

    return res


def dimensions_in_range(x, y, z):
    return x in range(size) \
           and y in range(size) \
           and z in range(size)


size = int(input())
cube = create_cube(size)
commands = read_commands()
curr_x, curr_y, curr_z = get_snakes_position(cube, size)
points_collected = 0
is_dead = False

for i in range(len(commands) - 1):

    if is_dead:
        break

    direction = commands[i].split()[0]
    steps = int(commands[i+1].split()[2])
    next_move_dimensions = get_next_move_dimensions(direction)

    for step in range(steps):
        next_x = curr_x + next_move_dimensions[0]
        next_y = curr_y + next_move_dimensions[1]
        next_z = curr_z + next_move_dimensions[2]

        if not dimensions_in_range(next_z, next_y, next_z):
            is_dead = True
            break

        else:
            if cube[next_x][next_y][next_z] == "a":
                cube[next_x][next_y][next_z] = "0"
                points_collected += 1

        curr_x = next_x
        curr_y = next_y
        curr_z = next_z


if is_dead:
    print(f"Points collected: {points_collected}\nThe snake dies.")

else:
    print(f"Points collected: {points_collected}")