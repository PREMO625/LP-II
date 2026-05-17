# Oral Viva Guide - Assignment 1 (BFS and DFS)

## Quick One-Liners

- **BFS**: Level-order traversal using a queue (FIFO).
- **DFS**: Deep traversal using a stack (LIFO) or recursion.
- **BFS shortest path**: Yes, but only for unweighted graphs.
- **DFS shortest path**: Not guaranteed.
- **Visited set**: Prevents cycles and infinite loops.

---

## Core Concept Questions

**Q1. What is a graph?**
A graph is a set of vertices (nodes) connected by edges.

**Q2. What is graph traversal?**
Systematically visiting all vertices in a graph.

**Q3. What is BFS?**
BFS explores neighbors level by level using a queue.

**Q4. What is DFS?**
DFS explores as deep as possible along one branch before backtracking.

**Q5. Why are BFS and DFS called uninformed search?**
They do not use heuristic information about the goal.

**Q6. What is the difference between BFS and DFS?**
BFS is level-wise and uses a queue; DFS is depth-wise and uses a stack/recursion.

---

## Data Structure Questions

**Q7. Why does BFS use a queue?**
Queue preserves FIFO order, which ensures level-by-level expansion.

**Q8. Why does DFS use a stack?**
Stack preserves LIFO order, which naturally supports depth-first traversal.

**Q9. Why use a `deque` in Python for BFS?**
`deque` supports fast O(1) pops from the left, unlike a list.

---

## Implementation-Specific Questions (Code-Oriented)

**Q10. Why do we use an adjacency list instead of adjacency matrix?**
Adjacency lists are memory-efficient for sparse graphs and easy to traverse.

**Q11. Why do we add both `u -> v` and `v -> u`?**
The graph is undirected, so edges are bidirectional.

**Q12. Why do we keep a `visited` set?**
To avoid revisiting nodes and prevent infinite loops in cyclic graphs.

**Q13. Why do we mark a node as visited before enqueueing/pushing?**
It prevents the same node from being added multiple times.

**Q14. Why is `reversed(self.graph[node])` used in DFS?**
To maintain a predictable traversal order based on the input order of neighbors.

---

## Working and Flow Questions

**Q15. How does BFS work step by step?**
Start at source, mark visited, enqueue it, then repeatedly dequeue and enqueue unvisited neighbors.

**Q16. How does DFS work step by step?**
Start at source, push onto stack, pop and visit, then push unvisited neighbors, and repeat.

**Q17. What happens if the graph is disconnected?**
Traversal covers only the connected component of the starting node.

**Q18. How do you traverse a disconnected graph?**
Run BFS/DFS from every unvisited node.

---

## Complexity Questions

**Q19. What is the time complexity of BFS and DFS?**
Both are $O(V + E)$.

**Q20. What is the space complexity of BFS?**
$O(V)$ for visited and queue storage.

**Q21. What is the space complexity of DFS?**
$O(V)$ for visited and stack/recursion.

---

## BFS vs DFS Practical Questions

**Q22. Which algorithm finds the shortest path in an unweighted graph?**
BFS.

**Q23. Which algorithm is better for deep graphs?**
DFS, because it uses less memory than BFS.

**Q24. Which algorithm is complete?**
BFS is complete; DFS may fail in infinite-depth graphs.

---

## Edge-Case and Tricky Questions

**Q25. What happens if you do not use a visited set?**
The traversal may loop forever in graphs with cycles.

**Q26. Can BFS be implemented recursively?**
Possible but inefficient; iterative queue-based implementation is preferred.

**Q27. Can DFS be implemented recursively?**
Yes, recursion naturally implements the stack behavior of DFS.

---

## Application Questions

**Q28. Where is BFS used in real life?**
Shortest path in unweighted graphs, social networks, web crawling.

**Q29. Where is DFS used in real life?**
Maze solving, backtracking, topological sorting, puzzle solving.

---

## Code Behavior Questions

**Q30. What does the `add_edge` function do?**
Adds an undirected edge by updating adjacency lists for both nodes.

**Q31. Why do we print nodes as we visit them?**
To show the traversal order of BFS/DFS.

**Q32. What would change if the graph were directed?**
We would add only `u -> v`, not `v -> u`.

---

## Suggested Viva Follow-Ups

**Q33. Why is BFS optimal in unweighted graphs?**
It explores nodes in increasing edge count order, so the first time you reach a node is the shortest path.

**Q34. Why can DFS miss the shortest path?**
It may go deep into a longer path before exploring shorter alternatives.

**Q35. How do BFS and DFS differ from Dijkstra's algorithm?**
Dijkstra handles weighted graphs using a priority queue, while BFS/DFS do not use weights.

---

## Closing Summary

BFS uses a queue to traverse level by level and guarantees shortest paths in unweighted graphs. DFS uses a stack or recursion to explore deeply and is memory-efficient for deep graphs, but it does not guarantee the shortest path. Both require a visited set to avoid infinite loops.
