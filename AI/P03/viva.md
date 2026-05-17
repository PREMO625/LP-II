# Oral Viva Guide - Assignment 3 (Prim's MST)

## Quick One-Liners

- **Prim's Algorithm**: Greedy algorithm to build MST by adding the smallest edge each step.
- **MST**: Connects all vertices with minimum total cost and no cycles.
- **MST edges**: Always $V - 1$.
- **Key idea**: Always connect a new vertex using the smallest valid edge.

---

## Core Concept Questions

**Q1. What is a Minimum Spanning Tree (MST)?**
A tree that connects all vertices with minimum total edge weight and no cycles.

**Q2. Why is Prim's algorithm greedy?**
It always chooses the smallest available edge at each step without looking ahead.

**Q3. Does Prim's work on directed graphs?**
No, it is designed for connected, weighted, undirected graphs.

**Q4. How many edges are in an MST?**
$V - 1$.

---

## Code-Oriented Questions (This Implementation)

**Q5. Why use an adjacency matrix?**
Simple and direct for small graphs; easy to check weights.

**Q6. Why do we keep a `selected` array?**
It tracks which vertices are already in the MST to avoid cycles.

**Q7. Why start from vertex 0?**
Any vertex can be the start; MST cost is the same for a connected graph.

**Q8. Why is `minimum` initialized to a large number (9999)?**
To ensure any real edge weight will be smaller and replace it.

**Q9. Why do we loop until `edges < vertices - 1`?**
An MST must have exactly $V - 1$ edges.

**Q10. How is a cycle avoided in the code?**
Only edges from selected to unselected vertices are chosen.

---

## Working Flow Questions

**Q11. Explain Prim's algorithm step-by-step.**
Start with one vertex, repeatedly add the smallest edge connecting the current tree to a new vertex until all vertices are included.

**Q12. What happens if the graph is disconnected?**
Prim's cannot build a full MST; it will stop before covering all vertices.

---

## Complexity Questions

**Q13. What is the time complexity of this matrix version?**
$O(V^2)$.

**Q14. How can Prim's be optimized?**
By using a priority queue (min-heap) with adjacency lists.

---

## Comparison Questions

**Q15. Prim's vs Kruskal's?**
Prim's grows one tree from a start vertex; Kruskal's adds smallest edges globally.

**Q16. Why not BFS or DFS for MST?**
BFS/DFS ignore weights and do not minimize total cost.

---

## External Examiner Questions

**Q17. Can multiple MSTs exist?**
Yes, if multiple edges have equal weights.

**Q18. What is the goal of MST in real life?**
Minimize total cost in network design, wiring, or road planning.

---

## Common Student Mistakes

- Choosing edges between already selected vertices (creates cycles).
- Forgetting that MST needs exactly $V - 1$ edges.
- Using a directed graph.
- Wrong adjacency matrix values.

---

## Summary

Prim's algorithm builds the MST greedily by adding the minimum edge that connects a new vertex. This implementation uses an adjacency matrix, a selected array, and a loop that runs until $V - 1$ edges are chosen.
