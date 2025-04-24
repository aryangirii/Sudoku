from flask import Flask, render_template, request
import sudoku

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    difficulty = request.args.get("level", "easy")
    puzzle = sudoku.generate_puzzle(difficulty)
    return render_template("index.html", puzzle=puzzle, difficulty=difficulty)

@app.route("/solve", methods=["POST"])
def solve():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = request.form.get(f"cell{i}{j}")
            row.append(int(val) if val and val.isdigit() else 0)
        board.append(row)

    solved = sudoku.solve_board(board)
    return render_template("index.html", puzzle=solved, difficulty="custom")

if __name__ == '__main__':
    app.run(debug=True)
