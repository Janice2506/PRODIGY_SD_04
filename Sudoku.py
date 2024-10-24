def is_valid(board, row, col, num):
    # Check if the number is not repeated in the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number is not repeated in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is not repeated in the 3x3 sub-grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def find_empty_location(board):
    # Find the next empty location (marked by 0)
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None


def solve_sudoku(board):
    empty_loc = find_empty_location(board)
    if not empty_loc:
        # No empty location means the puzzle is solved
        return True

    row, col = empty_loc

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            # Recurse with the new board
            if solve_sudoku(board):
                return True

            # Backtrack if the current num doesn't lead to a solution
            board[row][col] = 0

    return False


def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 21)
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            print(board[row][col], end=" ")
        print()


# Sample unsolved Sudoku puzzle (0 represents empty cells)
unsolved_board = [
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

# Solve the Sudoku puzzle
if solve_sudoku(unsolved_board):
    print("Solved Sudoku puzzle:")
    print_board(unsolved_board)
else:
    print("No solution exists.")
