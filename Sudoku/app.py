from flask import Flask, render_template, redirect, url_for
import sudoku

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('level'))

@app.route('/level')
def level():
    return render_template('level.html')

@app.route('/game/<level>')
def game(level):
    puzzle, solution = sudoku.generate_sudoku(level)
    return render_template('game.html', puzzle=puzzle, solution=solution, level=level)

if __name__ == '__main__':
    app.run(debug=True)
