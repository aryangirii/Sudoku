from flask import Flask, render_template, request, redirect, url_for, session
from sudoku import generate_puzzle, solve_board

app = Flask(__name__)
app.secret_key = 'sudoku-secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/level')
def level():
    return render_template('level.html')

@app.route('/game', methods=['POST'])
def game():
    level = request.form.get('level')
    puzzle = generate_puzzle(level)
    session['puzzle'] = puzzle
    session['solution'] = solve_board([row[:] for row in puzzle])
    return render_template('game.html', puzzle=puzzle, level=level)

if __name__ == '__main__':
    app.run(debug=True)
