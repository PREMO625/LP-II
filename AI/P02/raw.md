## Assignment No. 2

### Title

Implementation of A* Algorithm for Game Search Problem

### Aim

To implement the A* (A-Star) algorithm for finding the shortest and optimal path in a graph-based game search problem.

### Objectives

- Understand informed search algorithms.
- Implement the A* search algorithm.
- Find the shortest path between source and destination.
- Understand heuristic functions in AI.
- Compare path costs using heuristic and actual costs.

### Problem Statement

Implement the A* algorithm for any game search problem using weighted graph traversal and heuristic-based optimal searching.

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

### Introduction to A* Algorithm

#### Beginner Explanation

A* (A-Star) is one of the most famous Artificial Intelligence search algorithms used to find the shortest path between two points.

Examples:

- Google Maps finding shortest route.
- Game characters finding shortest movement path.
- Robots navigating obstacles.

A* helps in all these problems. It intelligently chooses the best path using:

- Actual distance travelled.
- Estimated distance remaining.

This makes A* faster and smarter than normal search algorithms.

#### Technical Definition

A* is an informed search algorithm that uses:

- Path cost.
- Heuristic estimation.

to efficiently compute the optimal path.

The evaluation function is:

$$
f(n) = g(n) + h(n)
$$

Where:

| Term | Meaning |
| --- | --- |
| $g(n)$ | Actual cost from start node to current node |
| $h(n)$ | Heuristic estimated cost to goal |
| $f(n)$ | Total estimated cost |

#### Core Concept

The algorithm always chooses the node having minimum $f(n)$. This helps the algorithm move toward the goal optimally.

### Working of A* Algorithm

#### Step-by-Step Flow

```text
Start Node
↓
Calculate f(n)
↓
Visit Neighbor Nodes
↓
Choose Node with Lowest f(n)
↓
Repeat Process
↓
Reach Goal Node
↓
Return Optimal Path
```

### Important Components

1. **Open List**: Contains nodes that need exploration.
2. **Closed List**: Contains already explored nodes.
3. **Heuristic Function**: Estimates distance to goal.

Examples of heuristics:

- Manhattan Distance.
- Euclidean Distance.

#### Why Heuristic Is Important

Without heuristic:

- Algorithm becomes slow.

With heuristic:

- Search becomes intelligent.
- Unnecessary paths are avoided.

### Admissible Heuristic

A heuristic is admissible if:

$$
h(n) \le h^*(n)
$$

Meaning the heuristic never overestimates actual cost. This guarantees an optimal solution.

### Advantages of A* Algorithm

- Finds shortest path.
- Complete algorithm.
- Optimal algorithm.
- Faster than uninformed search.
- Widely used in games and robotics.

### Disadvantages of A* Algorithm

- High memory usage.
- Slower for huge graphs.
- Performance depends on heuristic.
- Complex for large-scale systems.

### Real World Applications

| Application | Usage |
| --- | --- |
| Google Maps | Route optimization |
| Games | Character movement |
| Robotics | Robot navigation |
| GPS Systems | Shortest path |
| AI Agents | Intelligent searching |

### Architecture Diagram

```text
Graph Nodes
↓
Start Node
↓
Calculate g(n)
↓
Calculate h(n)
↓
Compute f(n)
↓
Choose Minimum f(n)
↓
Goal Reached
```

## Graph Used in Program

### Example Graph

```text
A -----1----- B
|             |
5             7
|             |
C -----10---- D
```

### Heuristic Values

| Node | Heuristic |
| --- | --- |
| A | 6 |
| B | 4 |
| C | 2 |
| D | 0 |

### Project Structure

```text
AStar_Project
│
├── astar.py
├── README.md
└── output.txt
```

## Correct Understanding of Problem Statement

The practical specifically says:

- Implement A* algorithm.
- Use weighted graph.
- Perform optimal searching.

So the code should:

- Use weighted edges.
- Use heuristic values.
- Compute $f(n) = g(n) + h(n)$.
- Find shortest path logically.

## Simplified and Correct Python Implementation

```python
import heapq

# Graph representation using dictionary
graph = {
    "A": [("B", 1), ("C", 5)],
    "B": [("D", 7)],
    "C": [("D", 10)],
    "D": [],
}

# Heuristic values
heuristic = {
    "A": 6,
    "B": 4,
    "C": 2,
    "D": 0,
}


# A* Algorithm
def astar(start, goal):
    # Priority queue
    open_list = []

    # Push starting node
    heapq.heappush(open_list, (0, start))

    # Store path
    came_from = {}

    # Store actual cost
    g_cost = {start: 0}

    while open_list:
        # Get node with lowest f(n)
        current_f, current_node = heapq.heappop(open_list)

        # Goal check
        if current_node == goal:
            path = []

            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]

            path.append(start)
            path.reverse()

            return path

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            tentative_g = g_cost[current_node] + weight

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                came_from[neighbor] = current_node
                g_cost[neighbor] = tentative_g

                f_cost = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))

    return None


# Driver Code
start_node = "A"
goal_node = "D"

path = astar(start_node, goal_node)

print("Shortest Path :", " -> ".join(path))
```

## Why This Code Is Better for Practical Exam

The original pseudo code in the PDF is incomplete, contains syntax issues, uses undefined variables, and is not easy to explain in viva.

This Python version:

- Correctly implements A*.
- Is easy to understand.
- Uses proper heuristic logic.
- Uses weighted graph.
- Matches problem statement.
- Is beginner friendly.
- Is viva friendly.

## Line-by-Line Code Explanation

### Import Library

```python
import heapq
```

Used for priority queue implementation. Priority queue always selects minimum cost node.

### Graph Definition

```python
graph = {
    "A": [("B", 1), ("C", 5)],
```

Represents a weighted graph. Format: `Node: [(Neighbor, Weight)]`.

### Heuristic Dictionary

```python
heuristic = {
```

Stores estimated distance to goal.

### A* Function

```python
def astar(start, goal):
```

Defines A* algorithm with parameters `start` (source node) and `goal` (destination node).

### Open List

```python
open_list = []
```

Stores nodes to be explored.

### Push Start Node

```python
heapq.heappush(open_list, (0, start))
```

Adds start node into priority queue.

### g_cost

```python
g_cost = {start: 0}
```

Stores actual cost from source.

### Pop Lowest Cost Node

```python
current_f, current_node = heapq.heappop(open_list)
```

Selects node with minimum $f(n)$.

### Goal Condition

```python
if current_node == goal:
```

Checks whether destination reached.

### Explore Neighbor Nodes

```python
for neighbor, weight in graph[current_node]:
```

Visits connected nodes.

### Calculate Actual Cost

```python
tentative_g = g_cost[current_node] + weight
```

Computes path cost.

### Calculate Final Cost

```python
f_cost = tentative_g + heuristic[neighbor]
```

Implements $f(n) = g(n) + h(n)$.

## Execution Flow

```text
Start A
↓
Visit B and C
↓
Calculate Costs
↓
Choose Lower Cost Node
↓
Move Toward Goal
↓
Reach D
↓
Print Shortest Path
```

## Expected Output

```text
Shortest Path : A -> B -> D
```

### Output Explanation

Path chosen:

A → B → D

Because:

| Path | Cost |
| --- | --- |
| A → B → D | 8 |
| A → C → D | 15 |

Algorithm selects minimum cost path.

## Time Complexity

| Case | Complexity |
| --- | --- |
| Worst Case | $O(E \log V)$ |

Where:

- $E$ = edges
- $V$ = vertices

## Space Complexity

| Complexity |
| --- |
| $O(V)$ |

## Difference Table

### BFS vs DFS vs A*

| Feature | BFS | DFS | A* |
| --- | --- | --- | --- |
| Uses Heuristic | No | No | Yes |
| Optimal | Yes | No | Yes |
| Fast | Moderate | Fast | Faster |
| Intelligent | No | No | Yes |

### A* vs Dijkstra

| Feature | A* | Dijkstra |
| --- | --- | --- |
| Uses Heuristic | Yes | No |
| Faster | Yes | No |
| Path Finding | Intelligent | Exhaustive |

## Common Viva Questions

### Basic Viva

**What is A* Algorithm?**

A* is an informed search algorithm used for finding shortest path using a heuristic function.

**Why is A* called informed search?**

Because it uses heuristic information to guide the search.

**What is heuristic?**

Estimated cost from current node to goal.

**What is g(n)?**

Actual cost from source node.

**What is h(n)?**

Estimated cost to destination.

**What is f(n)?**

Total estimated cost.

### Advanced Viva Questions

**Why is A* optimal?**

Because it selects path with minimum total estimated cost.

**What happens if heuristic overestimates?**

Algorithm may fail to find optimal path.

**What is admissible heuristic?**

A heuristic that never overestimates actual cost.

**Why use priority queue?**

To efficiently select minimum cost node.

### External Examiner Questions

| Question | Expected Answer |
| --- | --- |
| Why not use BFS? | BFS ignores weights |
| Why not use DFS? | DFS may not find shortest path |
| Why heuristic needed? | To speed up search |
| Can A* fail? | Yes if heuristic is poor |
| Is A* complete? | Yes |

## Common Student Mistakes

| Mistake | Problem |
| --- | --- |
| Forgetting heuristic | Becomes Dijkstra |
| Wrong $f(n)$ formula | Incorrect path |
| Using normal queue | Priority selection fails |
| Not updating `g_cost` | Wrong shortest path |

## Important One-Liners

| Question | Quick Answer |
| --- | --- |
| A* Formula | $f(n) = g(n) + h(n)$ |
| $g(n)$ | Actual cost |
| $h(n)$ | Heuristic estimate |
| A* Type | Informed search |
| Data Structure Used | Priority Queue |

## Conclusion

Successfully implemented the A* algorithm using weighted graph traversal and heuristic-based searching to obtain the shortest and optimal path between source and destination nodes.