import random


def generate_puzzle(level):
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_board(board)
    
    if level == 'easy':
        removals = 30
    elif level == 'medium':
        removals = 40
    else:
        removals = 50

    while removals > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            removals -= 1

    return board


def solve_board(board):
    empty = find_empty(board)
    if not empty:
        return board

    row, col = empty
    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num
            if solve_board(board):
                return board
            board[row][col] = 0

    return False


def valid(board, num, pos):
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None
