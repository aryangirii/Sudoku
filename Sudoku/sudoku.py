import random

# Function to generate a random Sudoku puzzle
def generate_puzzle(level='easy'):
    puzzle = [[0 for _ in range(9)] for _ in range(9)]
    solution = [[0 for _ in range(9)] for _ in range(9)]
    
    # Generate a valid solution for the Sudoku puzzle
    fill_grid(solution)
    
    # Remove some numbers to create the puzzle based on difficulty
    remove_numbers(puzzle, level)
    
    return puzzle, solution

def fill_grid(grid):
    """Fills a 9x9 Sudoku grid with a valid solution"""
    for i in range(9):
        for j in range(9):
            possible_values = list(range(1, 10))
            random.shuffle(possible_values)
            for value in possible_values:
                if is_valid(grid, i, j, value):
                    grid[i][j] = value
                    break
    return grid

def remove_numbers(grid, level='easy'):
    """Removes numbers from the grid based on difficulty"""
    if level == 'easy':
        num_to_remove = 30
    elif level == 'medium':
        num_to_remove = 40
    elif level == 'hard':
        num_to_remove = 50

    removed = 0
    while removed < num_to_remove:
        i, j = random.randint(0, 8), random.randint(0, 8)
        if grid[i][j] != 0:
            grid[i][j] = 0
            removed += 1

def is_valid(grid, row, col, num):
    """Checks if placing a number in a specific cell is valid"""
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    box_row, box_col = row // 3 * 3, col // 3 * 3
    for i in range(3):
        for j in range(3):
            if grid[box_row + i][box_col + j] == num:
                return False
    return True
