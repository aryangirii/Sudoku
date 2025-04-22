import random
import copy

def generate_full_board():
    board = [[0] * 9 for _ in range(9)]
    fill_board(board)
    return board

def fill_board(board):
    num_list = list(range(1, 10))
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                random.shuffle(num_list)
                for num in num_list:
                    if is_valid(board, num, (i, j)):
                        board[i][j] = num
                        if fill_board(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def generate_puzzle():
    board = generate_full_board()
    puzzle = copy.deepcopy(board)
    attempts = 40
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while puzzle[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        puzzle[row][col] = 0
        attempts -= 1
    return puzzle

def is_valid(board, num, pos):
    row, col = pos
    for i in range(9):
        if board[row][i] == num and i != col:
            return False
        if board[i][col] == num and i != row:
            return False
    box_x, box_y = col // 3, row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, num, (row, col)):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return board
                        board[row][col] = 0
                return None
    return board
