# Oral Viva Guide - Assignment 4 (N-Queens)

## Quick One-Liners

- **N-Queens**: Place N queens so none attack each other.
- **Backtracking**: Undo a choice when it leads to failure.
- **Branch and Bound**: Prune invalid paths early.
- **Key idea**: One queen per column, check row and diagonals.

---

## Core Concept Questions

**Q1. What is the N-Queens problem?**
Place N queens on an $N \times N$ board so no two queens share a row, column, or diagonal.

**Q2. Why is N-Queens a CSP?**
It has variables (queens), domains (rows), and constraints (no attacks).

**Q3. What is backtracking?**
Trying a choice, and if it fails, undoing it and trying another.

**Q4. What is branch and bound?**
A technique that stops exploring a branch as soon as it violates constraints.

---

## Code-Oriented Questions

**Q5. Why do we place one queen per column?**
It automatically avoids column conflicts.

**Q6. Why do we only check the left side in `is_safe`?**
Queens are placed left to right, so only previous columns can contain queens.

**Q7. Why do we check diagonals?**
Queens attack diagonally; diagonal checks enforce constraints.

**Q8. What is the backtracking step in code?**
`board[row][col] = 0` removes a queen and tries another position.

**Q9. What is the base case?**
If `col >= N`, all queens are placed successfully.

---

## Working Flow Questions

**Q10. Explain the algorithm step by step.**
Place a queen in a safe row of the current column, recurse to the next column, and backtrack if needed.

**Q11. What happens if no safe row is found in a column?**
The algorithm backtracks to the previous column.

---

## Complexity Questions

**Q12. What is the time complexity?**
Worst case is $O(N!)$.

**Q13. What is the space complexity?**
$O(N^2)$ due to the board.

---

## Comparison Questions

**Q14. Why not brute force?**
It explores all permutations and is extremely slow.

**Q15. Backtracking vs Greedy?**
Backtracking revisits decisions; greedy does not.

---

## External Examiner Questions

**Q16. Can there be multiple solutions?**
Yes, depending on $N$.

**Q17. What if no solution exists?**
The algorithm returns False.

---

## Common Student Mistakes

- Forgetting to backtrack.
- Not checking diagonals.
- Wrong base case.
- Placing multiple queens in the same row.

---

## Summary

The algorithm places queens column by column, checks safety using row and diagonal rules, and backtracks when a choice fails. Early pruning makes it a branch-and-bound style approach.
