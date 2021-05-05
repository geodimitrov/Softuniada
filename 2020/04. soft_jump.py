'''
Solution 1 - using deque
'''

from collections import deque

def create_board(rows):
    result = []

    for row in range(rows):
        result.append(deque(el for el in input()))

    return result

def find_players_position(board, player):
    for r in range(rows - 1, rows):
        for c in range(columns):
            if board[r][c] == player:
                return r, c

def move_cells_in_row(board, row, steps):

    for s in range(steps):
        board[row].appendleft(board[row].pop())

def make_jump(board, player_position):
    global total_jumps
    curr_row, col = player_position

    if board[curr_row - 1][col] == step:

        if curr_row == rows - 1:
            board[curr_row][col] = "0"
        else:
            board[curr_row][col] = step

        board[curr_row - 1][col] = player
        total_jumps += 1
        return curr_row - 1, col

    return curr_row, col

def print_result(board, jumps):

    if jumps < len(board) - 1:
        print("Lose")
    else:
        print("Win")

    print(f"Total Jumps: {jumps}")
    print("\n".join(''.join(row) for row in board))


player = "S"
step = "-"
rows, columns = map(int, input().split())
board = create_board(rows)
player_position = find_players_position(board, player)
commands = int(input())
total_jumps = 0

for command in range(commands):

    row, steps = map(int, input().split())
    move_cells_in_row(board, row, steps)
    player_position = make_jump(board, player_position)

print_result(board, total_jumps)


'''
Solution 2 - using string manipulation
'''

def create_board(rows):
    result = []

    for row in range(rows):
        result.append([el for el in input()])

    return result

def find_players_position(board, player):
    for r in range(rows - 1, rows):
        for c in range(columns):
            if board[r][c] == player:
                return r, c


def move_cells_in_row(board, row, steps):
    moves = steps % len(board[row])
    for move in range(moves):
        board[row] = board[row][-1] + board[row][:len(board[row])- 1]


def make_jump(board, player_position):
    global total_jumps
    curr_row, col = player_position

    if board[curr_row - 1][col] == step:

        if curr_row == rows - 1:
            element = "0"
        else:
            element = step

        board[curr_row] = board[curr_row][:col] + element + board[curr_row][col + 1:]
        board[curr_row - 1] = board[curr_row - 1][:col] + player + board[curr_row - 1][col + 1:]
        total_jumps += 1
        return curr_row - 1, col

    return curr_row, col

def print_result(board, jumps):

    if jumps < len(board) - 1:
        print("Lose")
    else:
        print("Win")

    print(f"Total Jumps: {jumps}")
    print("\n".join(board))


player = "S"
step = "-"
rows, columns = map(int, input().split())
board = [input() for r in range(rows)]
player_position = find_players_position(board, player)
commands = int(input())
total_jumps = 0

for command in range(commands):

    row, steps = map(int, input().split())
    move_cells_in_row(board, row, steps)
    player_position = make_jump(board, player_position)

print_result(board, total_jumps)