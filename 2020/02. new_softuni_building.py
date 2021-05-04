# Solution 1

def calc_n_lines(size):
    return size + size // 2

def create_first_line(size):
    line = ["#"]
    for i in range(1, size):
        line.append(".")

    return line

def create_room(size, lines):
    result = []
    result.append(create_first_line(size))

    for r in range(lines - 1):
        line = ["." for i in range(size)]
        result.append(line)

    return result

seat = "#"
room_size = int(input())
lines = calc_n_lines(room_size)
room = create_room(room_size, lines)

for row in range(lines):
    for col in range(room_size):
        if room[row][col] == seat:

            if col + 4 in range(room_size):
                room[row][col + 4] = seat

            next_row = row + 1
            next_col = col - 1

            if next_row in range(lines) and next_col in range(room_size):
                room[next_row][next_col] = seat

print('\n'.join("".join(line) for line in room))



# # Solution 2

seat = "#"
width = int(input())
height = width + width // 2
room = []
room.append(["#"])

for i in range(1, width):
    room[0].append(".")

for _ in range(height - 1):
    line = ["." for i in range(width)]
    room.append(line)

for row in range(height):
    for col in range(width):

        if room[row][col] == seat:

            if col + 4 in range(width):
                room[row][col + 4] = seat

            if row + 1 in range(height) and col - 1 in range(width):
                room[row + 1][col - 1] = seat

print('\n'.join("".join(line) for line in room))