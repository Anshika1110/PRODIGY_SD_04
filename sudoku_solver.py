def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if 'num' is not in the current column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check if 'num' is not in the current 3x3 sub-box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board):
    # Find an empty cell
    empty = find_empty_location(board)
    if not empty:
        return True  # No empty space left, puzzle solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num  # Try this number

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Undo the move (backtracking)

    return False  # Trigger backtracking

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

def input_sudoku():
    print("Enter the Sudoku puzzle row by row, use 0 for empty cells:")
    board = []
    for i in range(9):
        while True:
            row = input(f"Enter row {i+1}: ").strip()
            if len(row) == 9 and all(c in '0123456789' for c in row):
                board.append([int(c) for c in row])
                break
            else:
                print("Invalid input. Please enter exactly 9 digits (0-9) for the row.")
    return board

# Main function to run the Sudoku solver
def main():
    puzzle = input_sudoku()
    if solve_sudoku(puzzle):
        print("Sudoku puzzle solved successfully:")
        print_board(puzzle)
    else:
        print("No solution exists for the given Sudoku puzzle.")

if __name__ == "__main__":
    main()
