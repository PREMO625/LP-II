# N-Queens Problem using Backtracking and Branch & Bound

# Number of Queens
N = 4

# Chessboard initialization
board = [[0 for _ in range(N)] for _ in range(N)]


# Function to check whether queen can be placed safely
def is_safe(row, col):

    # Check left side of row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:

        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Check lower-left diagonal
    i = row
    j = col

    while i < N and j >= 0:

        if board[i][j] == 1:
            return False

        i += 1
        j -= 1

    return True


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

            # Recursive call for next column
            if solve_nqueens(col + 1):
                return True

            # Backtracking step
            board[row][col] = 0

    return False


# Driver Code
if solve_nqueens(0):

    print("Solution:\n")

    for row in board:
        print(row)

else:
    print("Solution does not exist")