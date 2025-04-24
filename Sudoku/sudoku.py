from flask import Flask, render_template, request, redirect, url_for
import random
import copy

app = Flask(__name__)

# Sample puzzles by difficulty
puzzles = {
    'easy': [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ],
    'medium': [
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 9, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 4, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 3, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 2, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 1, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 3, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 0]
    ],
    'hard': [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 8, 5],
        [0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 7, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 1, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 7, 3],
        [0, 0, 2, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 9]
    ]
}

# Simple solver (for demonstration)
def solve(board):
    def is_valid(num, row, col):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        r, c = 3 * (row // 3), 3 * (col // 3)
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                if board[i][j] == num:
                    return False
        return True

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(num, i, j):
                        board[i][j] = num
                        if solve(board):
                            return board
                        board[i][j] = 0
                return False
    return board

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/level', endpoint='level')
def choose_level():
    return render_template('level.html')

@app.route('/game/<level>')
def game(level):
    if level not in puzzles:
        return redirect(url_for('level'))

    puzzle = copy.deepcopy(puzzles[level])
    solution = solve(copy.deepcopy(puzzle))
    return render_template('game.html', puzzle=puzzle, solution=solution, level=level)

if __name__ == '__main__':
    app.run(debug=True)
