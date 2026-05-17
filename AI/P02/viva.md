# Oral Viva Guide - Assignment 2 (A* Algorithm)

## Quick One-Liners

- **A***: Informed search using $f(n) = g(n) + h(n)$.
- **$g(n)$**: Actual cost from start to current node.
- **$h(n)$**: Heuristic estimate from current node to goal.
- **Admissible heuristic**: Never overestimates actual cost.
- **Priority queue**: Always expands the node with minimum $f(n)$.

---

## Core Concept Questions

**Q1. What is A* algorithm?**
An informed search algorithm that finds the optimal path using actual cost and heuristic estimate.

**Q2. Why is A* called informed search?**
It uses heuristic information to guide the search.

**Q3. What is the evaluation function in A*?**
$f(n) = g(n) + h(n)$.

**Q4. What is the role of $g(n)$?**
Tracks the exact cost from the start node to the current node.

**Q5. What is the role of $h(n)$?**
Estimates the remaining cost from the current node to the goal.

**Q6. What is $f(n)$?**
The total estimated cost of a path through node $n$.

---

## Implementation-Specific Questions (Code-Oriented)

**Q7. Why use a priority queue (`heapq`)?**
To always expand the node with the smallest $f(n)$ efficiently.

**Q8. Why do we store `g_cost` in a dictionary?**
To track the best known cost to each node and update if a cheaper path is found.

**Q9. What is the role of `came_from`?**
It stores parent links to reconstruct the final path after reaching the goal.

**Q10. Why do we push `(f_cost, node)` into the heap?**
The heap is ordered by the first tuple element, so it expands by lowest $f(n)$.

**Q11. Why do we check `tentative_g < g_cost[neighbor]`?**
To ensure we only update when a better (lower-cost) path is found.

**Q12. Why is the start node pushed with cost 0?**
Because $g(start) = 0$ and the algorithm builds from there.

---

## Working and Flow Questions

**Q13. Explain A* step by step.**
Start at the source, compute costs, expand the node with minimum $f(n)$, update neighbors, repeat until the goal is reached.

**Q14. How does the algorithm decide which node to visit next?**
It chooses the node with the smallest $f(n)$ in the open list.

**Q15. When does A* stop?**
When the goal node is popped from the priority queue.

**Q16. How is the final path reconstructed?**
By following `came_from` links backward from the goal to the start.

---

## Heuristic Questions

**Q17. What makes a heuristic admissible?**
$h(n) \le h^*(n)$ for all nodes, meaning it never overestimates the true cost.

**Q18. Why does admissibility matter?**
It guarantees that A* finds the optimal path.

**Q19. What happens if the heuristic overestimates?**
A* may return a suboptimal path.

**Q20. Give examples of heuristics.**
Manhattan distance, Euclidean distance.

---

## Graph and Cost Questions

**Q21. Why do we use a weighted graph?**
A* is designed to work with weighted edges to find minimal path cost.

**Q22. Why not use BFS for this problem?**
BFS ignores weights, so it may return a longer-cost path.

**Q23. Why not use DFS for this problem?**
DFS may miss the shortest path and is not optimal.

**Q24. How does A* compare to Dijkstra?**
A* uses heuristics to guide search; Dijkstra expands uniformly without heuristics.

---

## Complexity Questions

**Q25. What is the time complexity of A*?**
Worst case is $O(E \log V)$ using a binary heap.

**Q26. What is the space complexity of A*?**
$O(V)$ for open/closed structures and cost maps.

---

## Code Behavior Questions

**Q27. What happens if a node has no neighbors?**
It contributes no expansions and is effectively a dead end.

**Q28. Why do we return `None` if no path is found?**
To indicate failure when the graph does not connect start to goal.

**Q29. Why is `came_from` only updated on a better path?**
To ensure the reconstructed path is optimal.

**Q30. What would change if you removed the heuristic?**
It becomes Dijkstra's algorithm.

---

## Output Questions

**Q31. Why is the output path A -> B -> D?**
Its total cost (8) is lower than A -> C -> D (15).

**Q32. What does the printed path represent?**
The optimal sequence of nodes from start to goal.

---

## Suggested Viva Follow-Ups

**Q33. Can A* be used in real-time games?**
Yes, it is widely used for pathfinding in games.

**Q34. Why is memory usage high in A*?**
It keeps many nodes in the open list along with cost data.

**Q35. What is the open list and closed list?**
Open list holds frontier nodes; closed list holds fully expanded nodes (not explicitly stored in this implementation).

---

## Closing Summary

A* combines actual path cost and heuristic estimates to efficiently find optimal paths in weighted graphs. With an admissible heuristic and priority queue, it guarantees the shortest path while reducing unnecessary exploration compared to uninformed search.
