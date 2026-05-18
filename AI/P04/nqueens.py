# N-Queens Problem using Backtracking and Branch & Bound

# Number of Queens
N = 4

# Chessboard initialization
board = [[0 for _ in range(N)] for _ in range(N)]

# Branch and bound helpers
col_used = [False] * N
diag1_used = [False] * (2 * N - 1)
diag2_used = [False] * (2 * N - 1)


# Function to check whether queen can be placed safely
def is_safe(row, col):
    return not col_used[row] and not diag1_used[row + col] and not diag2_used[row - col + N - 1]


# Backtracking function
def solve_nqueens(col):

    # Base condition
    if col >= N:
        return True

    # Try placing queen in every row
    for row in range(N):

        # Check safe position
        if is_safe(row, col):

            # Place queen
            board[row][col] = 1
            col_used[row] = True
            diag1_used[row + col] = True
            diag2_used[row - col + N - 1] = True

            # Recursive call for next column
            if solve_nqueens(col + 1):
                return True

            # Backtracking step
            board[row][col] = 0
            col_used[row] = False
            diag1_used[row + col] = False
            diag2_used[row - col + N - 1] = False

    return False


# Driver Code
if solve_nqueens(0):

    print("Solution:\n")

    for row in board:
        print(row)

else:
    print("Solution does not exist")