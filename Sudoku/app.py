from flask import Flask, render_template, request, redirect, url_for
import sudoku

app = Flask(__name__)

@app.route("/")
def index():
    puzzle = sudoku.generate_puzzle()
    return render_template("index.html", puzzle=puzzle)

@app.route("/solve", methods=["POST"])
def solve():
    board = [[int(x) if x else 0 for x in request.form.getlist(f"cell{r}{c}")] for r in range(9) for c in range(9)]
    board = [board[i:i+9] for i in range(0, 81, 9)]
    solved_board = sudoku.solve_sudoku(board)
    return render_template("index.html", puzzle=solved_board)

if __name__ == "__main__":
    app.run(debug=True)
