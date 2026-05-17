## Assignment No. 3

### Title

Implementation of Prim's Minimum Spanning Tree Algorithm using Greedy Method

### Aim

To implement Prim's Minimum Spanning Tree algorithm using greedy technique.

### Objectives

- Understand greedy algorithms.
- Implement Prim's algorithm.
- Construct a Minimum Spanning Tree (MST).
- Minimize total edge cost in a graph.
- Understand graph traversal using a greedy approach.

### Problem Statement

Implement Greedy Search Algorithm using Prim's Minimum Spanning Tree algorithm for finding the MST of a weighted graph.

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
| RAM | 4 GB minimum |
| Device | PC / Laptop |

## Theory

### Greedy Algorithm

#### Beginner Explanation

A greedy algorithm solves problems step-by-step by always choosing the best immediate option. It does not deeply consider future consequences.

#### Real Life Example

If you are buying items with limited money, you choose the cheapest useful item first.

#### Technical Definition

A greedy algorithm builds a solution piece-by-piece by choosing the locally optimal choice at each stage.

#### Properties of Greedy Algorithm

| Property | Meaning |
| --- | --- |
| Local Optimal Choice | Best choice at the current step |
| Fast Execution | Less computation |
| Simplicity | Easy implementation |
| Not Always Globally Optimal | May fail for some problems |

#### Applications of Greedy Algorithms

| Application | Usage |
| --- | --- |
| Prim's Algorithm | MST |
| Kruskal's Algorithm | MST |
| Dijkstra Algorithm | Shortest Path |
| Job Scheduling | Profit optimization |
| Huffman Coding | Compression |

### Minimum Spanning Tree (MST)

A Minimum Spanning Tree is a subset of graph edges that:

- Connects all vertices.
- Contains no cycles.
- Has minimum total edge weight.

#### Important Conditions of MST

- All vertices are connected.
- No cycles exist.
- Total edge weight is minimum.

### Prim's Algorithm

#### Beginner Explanation

Prim's algorithm starts from one node and repeatedly selects the minimum weight edge that connects a new vertex to the growing tree.

#### Technical Definition

Prim's algorithm is a greedy algorithm used to find the MST of a connected weighted undirected graph.

#### Working Principle

Prim's algorithm maintains:

| Set | Meaning |
| --- | --- |
| Visited Set | Vertices already in MST |
| Unvisited Set | Vertices not included |

At each step:

- Choose the smallest edge.
- Connect a new vertex.
- Avoid cycles.

#### Prim's Algorithm Flow

```text
Start Vertex
-> Find Minimum Edge
-> Add Edge to MST
-> Add New Vertex
-> Repeat
-> All Vertices Connected
-> MST Generated
```

#### Architecture Diagram

```text
Weighted Graph
-> Initialize Starting Vertex
-> Find Minimum Edge
-> Add New Vertex
-> Update MST
-> Repeat Until Complete
```

#### Why Prim's Is Greedy

At every step it chooses the minimum immediate edge without checking all future possibilities.

### Advantages of Prim's Algorithm

- Simple implementation.
- Efficient for dense graphs.
- Produces optimal MST.
- Greedy and fast.

### Disadvantages of Prim's Algorithm

- Works only for connected graphs.
- Slower for sparse graphs.
- Requires weighted graph.

### Applications of Prim's Algorithm

| Application | Usage |
| --- | --- |
| Network Design | Internet cables |
| Electrical Wiring | Power distribution |
| Road Networks | Cost optimization |
| Telecommunications | Minimum cable cost |

## Important Note About Practical

The pseudo code in the journal is incomplete and not beginner friendly. The code below is a correct, simple, and viva-friendly implementation that matches the problem statement.

## Graph Used

```text
    2
A --|-- B
|       |
6       3
|       |
C --1-- D
```

## Project Structure

```text
Prims_MST_Project
│
├── prims.py
├── README.md
└── output.txt
```

## Simple and Viva-Friendly Python Code

```python
# Number of vertices
vertices = 4

# Graph represented as adjacency matrix
graph = [
    [0, 2, 6, 0],
    [2, 0, 0, 3],
    [6, 0, 0, 1],
    [0, 3, 1, 0]
]

# Array to track selected vertices
selected = [False] * vertices

# Start from first vertex
selected[0] = True

# Edge counter
edges = 0

# Total minimum cost
minimum_cost = 0

print("Edges in Minimum Spanning Tree:\n")

# Loop until V-1 edges selected
while edges < vertices - 1:

    minimum = 9999
    x = 0
    y = 0

    # Traverse selected vertices
    for i in range(vertices):

        if selected[i]:

            for j in range(vertices):

                # Select minimum edge
                if (not selected[j]) and graph[i][j]:

                    if minimum > graph[i][j]:

                        minimum = graph[i][j]
                        x = i
                        y = j

    print(f"{x} - {y} : {graph[x][y]}")

    minimum_cost += graph[x][y]

    selected[y] = True

    edges += 1

print("\nMinimum Cost =", minimum_cost)
```

## Line-by-Line Explanation

### Graph Representation

`graph` is an adjacency matrix storing weights between vertices.

### Selected Array

`selected` tracks which vertices are already included in the MST.

### Starting Vertex

`selected[0] = True` starts MST from the first vertex.

### While Loop

MST always contains $V - 1$ edges, so the loop runs until that count is reached.

### Greedy Edge Selection

```python
if minimum > graph[i][j]:
```

Chooses the smallest edge connecting a visited vertex to an unvisited vertex.

### Update MST Cost

```python
minimum_cost += graph[x][y]
```

Adds the chosen edge weight to the total cost.

## Execution Flow

```text
Start Vertex A
-> Find Minimum Edge
-> Add Edge to MST
-> Visit New Vertex
-> Repeat
-> All Vertices Connected
```

## Expected Output

```text
Edges in Minimum Spanning Tree:

0 - 1 : 2
1 - 3 : 3
3 - 2 : 1

Minimum Cost = 6
```

### Output Explanation

Selected edges (mapping 0=A, 1=B, 2=C, 3=D):

| Edge | Weight |
| --- | --- |
| A-B | 2 |
| B-D | 3 |
| D-C | 1 |

Total Cost = $2 + 3 + 1 = 6$.

## Time Complexity

| Case | Complexity |
| --- | --- |
| Worst Case | $O(V^2)$ |

## Space Complexity

| Complexity |
| --- |
| $O(V^2)$ |

## Difference Table

### Prim's vs Kruskal's

| Feature | Prim's | Kruskal's |
| --- | --- | --- |
| Approach | Vertex-based | Edge-based |
| Cycle Detection | Simpler | Required |
| Best For | Dense graphs | Sparse graphs |

### BFS vs DFS vs Prim's

| Feature | BFS | DFS | Prim's |
| --- | --- | --- | --- |
| Purpose | Traversal | Traversal | MST |
| Uses Weight | No | No | Yes |
| Greedy | No | No | Yes |

## Common Viva Questions

### Basic Viva

**What is MST?**
A tree connecting all vertices with minimum total weight and no cycles.

**Why is Prim's called greedy?**
Because it selects the minimum edge at every step.

**How many edges are in an MST?**
$V - 1$.

**Can MST contain cycles?**
No.

**Does Prim's work on directed graphs?**
No, it is mainly for undirected weighted graphs.

### Advanced Viva

**Why does Prim's avoid cycles?**
It only connects unvisited vertices.

**Difference between MST and shortest path?**
MST minimizes total tree cost, not source-to-destination path.

**Can multiple MSTs exist?**
Yes, if edge weights are equal.

**Why adjacency matrix used?**
It is simple for small graphs.

### External Examiner Trap Questions

| Question | Smart Answer |
| --- | --- |
| Why not use BFS? | BFS ignores weights |
| Why not DFS? | DFS does not minimize cost |
| Why no heap used? | Simpler implementation for understanding Prim's logic |
| Can Prim's be optimized? | Yes, using a min-heap or priority queue |

## Common Student Mistakes

| Mistake | Problem |
| --- | --- |
| Selecting already visited node | Cycle creation |
| Forgetting $V-1$ edges | Incomplete MST |
| Using directed graph | Incorrect result |
| Wrong graph matrix | Incorrect weights |

## Most Important One-Liners

| Question | Quick Answer |
| --- | --- |
| Prim's Type | Greedy Algorithm |
| Output | Minimum Spanning Tree |
| MST Edges | $V - 1$ |
| Graph Type | Weighted undirected graph |
| Goal | Minimum total cost |

## Conclusion

Successfully implemented Prim's Minimum Spanning Tree algorithm using greedy technique to generate MST with minimum total edge cost.
