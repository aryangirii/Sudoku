from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/game/<level>')
def game(level):
    # Generate puzzle and solution based on level
    puzzle, solution = generate_puzzle(level)
    return render_template('game.html', puzzle=puzzle, solution=solution, level=level)

@app.route('/')
def index():
    return redirect(url_for('game', level='easy'))

# Function to generate Sudoku puzzle and solution
def generate_puzzle(level):
    # Logic to generate puzzle and solution
    puzzle = [[0 for _ in range(9)] for _ in range(9)]  # Sample empty puzzle
    solution = [[1 for _ in range(9)] for _ in range(9)]  # Sample solution, you should replace with actual logic
    return puzzle, solution

if __name__ == "__main__":
    app.run(debug=True)
