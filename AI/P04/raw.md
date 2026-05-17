## Assignment No. 4

### Title

Implementation of N-Queens Problem using Backtracking and Branch and Bound

### Aim

To implement a solution for a constraint satisfaction problem using backtracking and branch and bound for the N-Queens problem.

### Objectives

- Understand constraint satisfaction problems (CSP).
- Implement backtracking algorithm.
- Solve the N-Queens problem.
- Understand branch and bound technique.
- Place N queens safely on a chessboard.

### Problem Statement

Implement a solution for a CSP using branch and bound and backtracking for the N-Queens problem.

### Software Requirements

| Requirement | Details |
| --- | --- |
| Operating System | Windows 7/8/10/11 |
| Programming Language | Python |
| IDE | VS Code / PyCharm |

### Hardware Requirements

| Requirement | Details |
| --- | --- |
| Processor | Intel Core i3/i5 or above |
| RAM | 4GB minimum |
| Device | PC / Laptop |

## Theory

### Constraint Satisfaction Problem (CSP)

#### Beginner Explanation

A CSP is a problem where some rules (constraints) exist and the solution must satisfy all rules.

Examples:

- Sudoku
- Timetable scheduling
- Graph coloring
- N-Queens

#### Technical Definition

A CSP consists of:

| Component | Meaning |
| --- | --- |
| $X$ | Variables |
| $D$ | Domains |
| $C$ | Constraints |

#### Components of CSP

- **Variables ($X$)**: Things we need to assign values to (queen positions).
- **Domains ($D$)**: Possible values (rows $0$ to $N-1$).
- **Constraints ($C$)**: Rules that must be satisfied (no attacks).

### N-Queens Problem

Place $N$ queens on an $N \times N$ chessboard such that:

- No two queens share the same row.
- No two queens share the same column.
- No two queens share the same diagonal.

Example for $N = 4$ (Q = Queen):

```text
_ Q _ _
_ _ _ Q
Q _ _ _
_ _ Q _
```

### Why N-Queens is CSP

- Queen positions are variables.
- Rows/columns are domains.
- Attack rules are constraints.

### Backtracking Algorithm

#### Beginner Explanation

Backtracking means:

- Try a solution.
- If wrong, go back and try another.

#### Backtracking Flow

```text
Place Queen
-> Check Safety
-> Safe? YES -> Move to Next Column
-> Safe? NO -> Backtrack and Try Another Position
```

### Branch and Bound

Branch and bound prunes invalid paths early instead of exploring every possibility.

### Difference Between Backtracking and Branch and Bound

| Backtracking | Branch and Bound |
| --- | --- |
| Goes deeper then returns | Prunes early |
| Trial and error | Optimization |
| Constraint checking | Bound checking |

### Important Constraints in N-Queens

Queens must NOT attack:

| Direction | Condition |
| --- | --- |
| Same Row | Row clash |
| Same Column | Column clash |
| Diagonal | Diagonal clash |

#### Mathematical Condition for Diagonal Attack

$$
|x_1 - x_2| = |y_1 - y_2|
$$

#### Why Column Clash Is Avoided Automatically

Because the algorithm places only one queen per column.

### Architecture Diagram

```text
Start
-> Place Queen
-> Check Constraints
-> Safe? YES -> Place Next Queen
-> Safe? NO -> Backtrack
-> Try Another Position
-> Solution Found
```

## Project Structure

```text
NQueens_Project
│
├── nqueens.py
├── README.md
└── output.txt
```

## Simple and Correct Python Code

```python
# Number of Queens
N = 4

# Chess board initialization
board = [[0 for i in range(N)] for j in range(N)]


# Function to check whether queen can be placed safely
def is_safe(row, col):

    # Check left side of row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:

        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    # Check lower diagonal
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

    # All queens placed
    if col >= N:
        return True

    # Try every row
    for row in range(N):

        # Check safe position
        if is_safe(row, col):

            # Place queen
            board[row][col] = 1

            # Recur for next column
            if solve_nqueens(col + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Driver Code
if solve_nqueens(0):

    print("Solution:\n")

    for row in board:
        print(row)

else:
    print("Solution does not exist")
```

## Why This Code Implements Backtracking

The key backtracking step is:

```python
board[row][col] = 0
```

It removes the previously placed queen and tries another position.

## Why This Is Also Branch and Bound Style

Unsafe positions are rejected early inside `is_safe`, pruning invalid branches.

## Line-by-Line Explanation

### Board Initialization

`board = [[0 for i in range(N)] for j in range(N)]` creates an $N \times N$ board.

### Safety Function

`is_safe(row, col)` checks row and diagonal constraints.

### Recursive Function

`solve_nqueens(col)` places queens column by column.

### Backtracking Step

`board[row][col] = 0` undoes a wrong placement.

## Execution Flow

```text
Start Column 0
-> Place Queen
-> Check Safety
-> Safe? YES -> Next Column
-> Unsafe? YES -> Backtrack
-> Try New Row
-> All Queens Placed
```

## Expected Output

```text
Solution:

[0, 0, 1, 0]
[1, 0, 0, 0]
[0, 0, 0, 1]
[0, 1, 0, 0]
```

### Output Explanation

1 represents queen placement. Queens are placed safely with no row, column, or diagonal attacks.

## Time Complexity

| Complexity |
| --- |
| $O(N!)$ |

## Space Complexity

| Complexity |
| --- |
| $O(N^2)$ |

## Difference Table

### Backtracking vs Greedy

| Feature | Backtracking | Greedy |
| --- | --- | --- |
| Revisits Decisions | Yes | No |
| Tries Alternatives | Yes | No |
| Uses Recursion | Usually | Not Necessary |
| Guarantees Solution | Often Yes | Not Always |

### Branch and Bound vs Backtracking

| Feature | Backtracking | Branch and Bound |
| --- | --- | --- |
| Main Goal | Feasible Solution | Optimal Solution |
| Pruning | Less | More |
| Search Space Reduction | Moderate | High |

## Common Viva Questions

### Basic Viva

**What is the N-Queens problem?**
Place $N$ queens safely on the chessboard.

**Why is N-Queens a CSP?**
Because constraints must be satisfied.

**What is backtracking?**
Undoing wrong choices and trying alternatives.

**Why is recursion used?**
To explore possible queen placements.

**What is branch and bound?**
A technique that prunes invalid paths early.

### Advanced Viva

**Why only left side is checked?**
Because queens are placed column by column from left to right.

**Why diagonal checking needed?**
Queens attack diagonally.

**Can multiple solutions exist?**
Yes.

**What happens if no solution exists?**
The algorithm returns False.

### External Examiner Trap Questions

| Question | Smart Answer |
| --- | --- |
| Why not brute force? | Too many permutations |
| Why recursion used? | Natural for backtracking |
| What is pruning? | Rejecting invalid states early |
| Why $O(N!)$ complexity? | Multiple recursive possibilities |

## Common Student Mistakes

| Mistake | Problem |
| --- | --- |
| Forgetting backtracking step | Wrong board state |
| Not checking diagonals | Invalid solution |
| Incorrect recursion base case | Infinite recursion |
| Multiple queens in same row | Constraint violation |

## Most Important One-Liners

| Question | Quick Answer |
| --- | --- |
| Problem Type | CSP |
| Algorithm Used | Backtracking |
| Optimization Idea | Branch and Bound |
| Queen Attack Directions | Row, Column, Diagonal |
| Time Complexity | $O(N!)$ |

## Conclusion

Successfully implemented the N-Queens problem using backtracking and branch and bound techniques.
