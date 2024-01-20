def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

def is_safe(board, row, col, num):
    # Check if the number is not present in the current row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the number is not present in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board, empty_location):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                empty_location[0] = i
                empty_location[1] = j
                return True
    return False

def solve_sudoku(board):
    empty_location = [0, 0]

    if not find_empty_location(board, empty_location):
        # All cells are filled; Sudoku solved
        return True

    row, col = empty_location[0], empty_location[1]

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            # If placing the current number does not lead to a solution, backtrack
            board[row][col] = 0

    # No solution found
    return False

# Example Sudoku board (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Original Sudoku Board:")
print_board(sudoku_board)
print("\nSolving Sudoku...\n")

if solve_sudoku(sudoku_board):
    print("Sudoku Solved:")
    print_board(sudoku_board)
else:
    print("No solution exists.")
