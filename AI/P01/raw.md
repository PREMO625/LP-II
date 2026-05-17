# Assignment No. 1

# Title
Implementation of Breadth First Search (BFS) and Depth First Search (DFS) Algorithms using Graph in Artificial Intelligence

---

# Aim
To implement Breadth First Search (BFS) and Depth First Search (DFS) algorithms using an undirected graph and understand graph traversal techniques used in Artificial Intelligence.

---

# Objectives
1. To understand graph traversal techniques.
2. To study uninformed search algorithms in Artificial Intelligence.
3. To implement BFS and DFS algorithms.
4. To understand searching in graphs and trees.
5. To compare BFS and DFS based on performance and working.
6. To analyze time complexity and space complexity of search algorithms.
7. To understand practical applications of graph search in AI systems.

---

# Problem Statement
Implement Breadth First Search (BFS) and Depth First Search (DFS) algorithms using an undirected graph. Develop algorithms that traverse all vertices of the graph recursively or iteratively and analyze their working in Artificial Intelligence.

---

# Software Requirements
| Component | Requirement |
|---|---|
| Operating System | Windows 10/11, Linux, macOS |
| Programming Language | Python / C++ / Java |
| IDE/Editor | VS Code / PyCharm / IntelliJ |
| Python Version | Python 3.x |
| Libraries Required | collections |

---

# Hardware Requirements
| Component | Requirement |
|---|---|
| Processor | Intel i3/i5/i7 or above |
| RAM | Minimum 4 GB |
| Storage | 500 MB Free Space |
| Device | PC/Laptop |

---

# Theory

# Introduction to Artificial Intelligence Search

## Beginner Explanation
Artificial Intelligence systems often need to find solutions to problems.

Example:
- Google Maps finding shortest path.
- Chess AI finding best move.
- Robot finding route in a room.
- Social media recommending connections.

To solve such problems, AI uses searching algorithms.

Searching means:

> Exploring different possible paths or states until the required goal is found.

---

# What is Search in AI?

Search is a step-by-step process used to solve problems by exploring different possible states.

A search problem mainly contains:

| Component | Description |
|---|---|
| Search Space | Set of all possible solutions |
| Initial State | Starting point |
| Goal State | Desired final state |
| Path | Sequence of states |
| Cost Function | Measures expense of path |

---

# Search Space

Search space is the collection of all possible states that can be reached.

Example:

If a robot moves in a maze:

- Every room = state
- All rooms together = search space

---

# Search Tree

A search tree represents the exploration process.

Example:

Start Node
↓
Possible Moves
↓
Next States
↓
Goal State

---

# Types of Search Algorithms

## 1. Uninformed Search (Blind Search)

These algorithms do not know where the goal is.

They simply explore nodes.

Examples:
- BFS
- DFS
- Uniform Cost Search

### Features
- No heuristic used
- Simple implementation
- Can be slow for large problems

---

## 2. Informed Search (Heuristic Search)

These algorithms use additional knowledge.

Example:
- A* Algorithm
- Greedy Best First Search

### Features
- Faster
- Smarter exploration
- Uses heuristic function

---

# Breadth First Search (BFS)

## Beginner Explanation

BFS explores the graph level by level.

It first visits:
- immediate neighbors
- then neighbors of neighbors
- and so on.

It uses a Queue data structure.

---

# BFS Working

Suppose graph:

A → B → C
↓
D

Traversal:

A → B → D → C

---

# BFS Flow Diagram

Start Node
↓
Insert into Queue
↓
Visit Node
↓
Add Adjacent Nodes
↓
Repeat Until Queue Empty

---

# BFS Internal Working

1. Start from source node.
2. Mark node as visited.
3. Insert node into queue.
4. Remove node from queue.
5. Visit all adjacent unvisited nodes.
6. Insert adjacent nodes into queue.
7. Repeat until queue becomes empty.

---

# BFS Architecture

Graph
↓
Queue
↓
Level-wise Traversal
↓
Goal Found

---

# Advantages of BFS

| Advantage | Description |
|---|---|
| Complete | Finds solution if exists |
| Optimal | Gives shortest path in unweighted graph |
| Systematic | Traverses level by level |

---

# Disadvantages of BFS

| Disadvantage | Description |
|---|---|
| High Memory Usage | Stores many nodes |
| Slow for Large Graphs | Explores unnecessary nodes |

---

# Applications of BFS

1. Social networking
2. GPS navigation
3. Web crawling
4. AI game solving
5. Network broadcasting
6. Shortest path finding

---

# Depth First Search (DFS)

## Beginner Explanation

DFS goes deep into one branch before exploring another branch.

It uses Stack data structure.

---

# DFS Working

Example:

A → B → C
↓
D

Traversal:

A → B → C → D

---

# DFS Flow Diagram

Start Node
↓
Push into Stack
↓
Visit Node
↓
Go Deep into Branch
↓
Backtrack
↓
Repeat

---

# DFS Internal Working

1. Start from source node.
2. Mark node as visited.
3. Push node into stack.
4. Pop node from stack.
5. Visit adjacent unvisited node.
6. Continue deeper traversal.
7. Backtrack when no adjacent nodes remain.

---

# DFS Architecture

Graph
↓
Stack
↓
Deep Traversal
↓
Backtracking
↓
Goal Found

---

# Advantages of DFS

| Advantage | Description |
|---|---|
| Less Memory | Stores fewer nodes |
| Fast in Deep Graphs | Quickly reaches deep nodes |
| Easy Recursive Implementation | Simple coding |

---

# Disadvantages of DFS

| Disadvantage | Description |
|---|---|
| Not Optimal | May not find shortest path |
| Can Get Stuck | Infinite depth problems |
| Incomplete in Infinite Graph | May never terminate |

---

# Applications of DFS

1. Maze solving
2. Path finding
3. Cycle detection
4. Topological sorting
5. AI puzzle solving
6. Backtracking problems

---

# Difference Between BFS and DFS

| Feature | BFS | DFS |
|---|---|---|
| Full Form | Breadth First Search | Depth First Search |
| Data Structure | Queue | Stack |
| Traversal | Level-wise | Depth-wise |
| Memory Usage | High | Low |
| Shortest Path | Yes | No |
| Speed | Slower | Faster in deep graphs |
| Completeness | Complete | Not always complete |
| Optimality | Optimal | Non-optimal |

---

# Time Complexity

For both BFS and DFS:

genui{"math_block_widget_always_prefetch_v2":{"content":"O(V+E)"}}

Where:
- V = Number of vertices
- E = Number of edges

---

# Space Complexity

## BFS

genui{"math_block_widget_always_prefetch_v2":{"content":"O(V)"}}

Stores many nodes in queue.

## DFS

genui{"math_block_widget_always_prefetch_v2":{"content":"O(V)"}}

Stores nodes in recursion stack.

---

# Graph Representation

## Adjacency List

Example:

A → B, C
B → D
C → D
D → None

---

# AI Perspective of BFS and DFS

## BFS in AI

Used when:
- shortest path required
- all nearby states explored first

Examples:
- GPS
- Chatbot conversation graphs
- Recommendation systems

---

## DFS in AI

Used when:
- searching deep solutions
- memory optimization required

Examples:
- Puzzle solving
- Game trees
- Backtracking

---

# Architecture Diagram

Input Graph
↓
Graph Representation
↓
Traversal Algorithm
↓
Visited Nodes Tracking
↓
Output Traversal Sequence

---

# Execution Flow

User Input
↓
Create Graph
↓
Add Edges
↓
Choose BFS/DFS
↓
Traverse Nodes
↓
Display Result

---

# Project Structure

BFS_DFS_Project
├── bfs_dfs.py
├── README.md
├── output.txt
└── graph_input.txt

---

# Python Program for BFS and DFS

```python
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        visited.add(start)

        print("BFS Traversal:")

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self, start):
        visited = set()
        stack = [start]

        print("\nDFS Traversal:")

        while stack:
            node = stack.pop()

            if node not in visited:
                print(node, end=" ")
                visited.add(node)

                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

# Driver Code

g = Graph()

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('D', 'F')

g.bfs('A')
g.dfs('A')
```

---

# Line-by-Line Code Explanation

## Import Statement

```python
from collections import deque
```

- deque is a double-ended queue.
- Used for efficient BFS implementation.
- Queue operations become faster.

---

## Graph Class

```python
class Graph:
```

Defines graph structure.

---

## Constructor

```python
def __init__(self):
    self.graph = {}
```

- Initializes empty dictionary.
- Dictionary stores adjacency list.

---

## Add Edge Function

```python
def add_edge(self, u, v):
```

Adds connection between vertices.

---

## BFS Function

```python
def bfs(self, start):
```

Implements Breadth First Search.

---

## Queue Initialization

```python
queue = deque([start])
```

Stores nodes for BFS traversal.

---

## DFS Function

```python
def dfs(self, start):
```

Implements Depth First Search.

---

## Stack Initialization

```python
stack = [start]
```

Stores nodes for DFS traversal.

---

# Dataset and Input Explanation

The graph nodes act as dataset.

Example Input:

A-B
A-C
B-D
C-E
D-F

---

# Model Training Section

This practical does not involve machine learning model training.

However, search algorithms are foundational concepts used in:
- Reinforcement Learning
- Robotics
- Pathfinding
- Game AI
- State Space Exploration

---

# Output

## Expected Output

```text
BFS Traversal:
A B C D E F

DFS Traversal:
A B D F C E
```

---

# Output Explanation

## BFS Output

Visits nodes level-by-level.

Traversal Order:

A
↓
B, C
↓
D, E
↓
F

---

## DFS Output

Visits nodes deeply first.

Traversal Order:

A
↓
B
↓
D
↓
F
↓
Backtrack
↓
C
↓
E

---

# Real World Applications

| Domain | Usage |
|---|---|
| Google Maps | Shortest path finding |
| Facebook | Friend recommendations |
| Robotics | Navigation |
| Gaming | AI movement |
| Web Crawlers | Internet indexing |
| Networking | Packet routing |

---

# Advantages of Graph Search in AI

1. Efficient navigation.
2. Problem-solving capability.
3. Decision-making support.
4. Path optimization.
5. State-space exploration.

---

# Limitations

1. High memory consumption.
2. Large search spaces.
3. Infinite loops without visited tracking.
4. Computationally expensive for huge graphs.

---

# Common Student Mistakes

| Mistake | Explanation |
|---|---|
| Forgetting visited array | Causes infinite loop |
| Wrong queue usage in BFS | Incorrect traversal |
| Wrong stack usage in DFS | Traversal failure |
| Missing bidirectional edges | Incomplete graph |
| Not handling disconnected graph | Partial traversal |

---

# Viva Questions and Answers

# Basic Viva Questions

## 1. What is Artificial Intelligence?

Artificial Intelligence is a branch of computer science that enables machines to simulate human intelligence.

---

## 2. What is searching in AI?

Searching is the process of exploring states to find a goal state.

---

## 3. What is BFS?

BFS is a graph traversal algorithm that explores nodes level-by-level using queue.

---

## 4. What is DFS?

DFS is a graph traversal algorithm that explores nodes deeply using stack.

---

## 5. Why is queue used in BFS?

Queue follows FIFO order.
This ensures level-wise traversal.

---

## 6. Why is stack used in DFS?

Stack follows LIFO order.
This helps deep traversal.

---

## 7. Which algorithm gives shortest path?

BFS gives shortest path in unweighted graph.

---

## 8. What is a graph?

A graph is a non-linear data structure containing vertices and edges.

---

## 9. What is adjacency list?

Adjacency list stores neighboring nodes for every vertex.

---

## 10. What is time complexity of BFS and DFS?

genui{"math_block_widget_always_prefetch_v2":{"content":"O(V+E)"}}

---

# Intermediate Viva Questions

## 11. Difference between informed and uninformed search?

| Informed Search | Uninformed Search |
|---|---|
| Uses heuristic | No heuristic |
| Faster | Slower |
| Smarter decisions | Blind traversal |

---

## 12. What is heuristic function?

A heuristic estimates distance from current state to goal state.

---

## 13. Why visited array is important?

Prevents revisiting nodes and infinite loops.

---

## 14. Can DFS find shortest path?

No, DFS does not guarantee shortest path.

---

## 15. What happens if graph has cycle?

Without visited tracking, traversal may become infinite.

---

# Advanced External Viva Questions

## 16. Why BFS is optimal?

Because it explores nodes level-by-level and first discovered solution has minimum edges.

---

## 17. Why BFS consumes more memory?

Because it stores all neighboring nodes in queue simultaneously.

---

## 18. Which algorithm is better for deep graphs?

DFS is better for deep graphs due to low memory usage.

---

## 19. Can BFS be implemented recursively?

Possible but inefficient.
Queue-based iterative implementation preferred.

---

## 20. What are applications of DFS in compilers?

DFS is used in:
- topological sorting
- dependency resolution
- syntax tree traversal

---

# Code-Related Viva Questions

## 21. Why deque used instead of list?

deque provides faster insertion and deletion from front.

---

## 22. Why set used for visited?

Set provides fast lookup.

---

## 23. Why reversed used in DFS?

Maintains expected traversal order.

---

## 24. What happens if graph is disconnected?

Traversal covers only connected component.

---

## 25. How to traverse disconnected graph?

Run traversal for every unvisited node.

---

# Tricky External Questions

## 26. Which algorithm is complete?

BFS is complete.
DFS may fail in infinite-depth graphs.

---

## 27. Can BFS work on weighted graph?

Not efficiently.
Dijkstra’s algorithm preferred.

---

## 28. What is backtracking in DFS?

Returning to previous node after reaching dead end.

---

## 29. Which data structure internally uses DFS?

Trees and recursive algorithms.

---

## 30. Explain BFS mathematically.

BFS explores all nodes at depth d before moving to d+1.

---

# Quick Revision Table

| Question | Quick Answer |
|---|---|
| BFS uses? | Queue |
| DFS uses? | Stack |
| BFS traversal? | Level-wise |
| DFS traversal? | Depth-wise |
| BFS shortest path? | Yes |
| DFS shortest path? | No |
| Time complexity? | O(V+E) |
| BFS memory? | High |
| DFS memory? | Low |
| BFS complete? | Yes |

---

# Common External Examiner Questions

1. Why BFS guarantees shortest path?
2. Why DFS may fail?
3. Difference between tree and graph traversal?
4. Why recursion used in DFS?
5. Explain stack overflow in DFS.
6. Explain cycle detection.
7. What is branching factor?
8. Explain state-space representation.
9. Why BFS expensive in memory?
10. Applications in AI?

---

# Memory Tricks

## BFS

Breadth = Width

So BFS explores width-wise.

Queue = FIFO.

---

## DFS

Depth = Deep.

DFS goes deep.

Stack = LIFO.

---

# Conclusion

In this practical, Breadth First Search (BFS) and Depth First Search (DFS) algorithms were implemented successfully using graph traversal techniques. The practical helped in understanding uninformed search algorithms used in Artificial Intelligence. BFS explores nodes level-by-level using queue, while DFS explores deeply using stack or recursion. Both algorithms are fundamental in AI, robotics, networking, gaming, and pathfinding applications.

---

# Final Quick Revision

| Topic | Key Point |
|---|---|
| BFS | Level-order traversal |
| DFS | Deep traversal |
| Queue | Used in BFS |
| Stack | Used in DFS |
| BFS Advantage | Shortest path |
| DFS Advantage | Less memory |
| BFS Limitation | High memory |
| DFS Limitation | Not optimal |
| AI Use | Pathfinding |
| Complexity | O(V+E) |

---

# Important Keywords

- Artificial Intelligence
- Search Algorithms
- BFS
- DFS
- Graph Traversal
- Queue
- Stack
- Search Space
- State Space
- Path Finding
- Heuristic Search
- Uninformed Search
- Graph Theory
- Adjacency List
- Backtracking

