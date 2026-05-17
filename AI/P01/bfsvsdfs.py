from collections import deque

# Graph Class
class Graph:

    # Constructor
    def __init__(self):
        self.graph = {}

    # Function to add edge in undirected graph
    def add_edge(self, u, v):

        # Create adjacency list if vertex not present
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        # Add edges for undirected graph
        self.graph[u].append(v)
        self.graph[v].append(u)

    # Breadth First Search (BFS)
    def bfs(self, start):

        visited = set()              # Store visited nodes
        queue = deque([start])       # Initialize queue

        visited.add(start)

        print("BFS Traversal:")

        while queue:

            # Remove first element from queue
            node = queue.popleft()

            print(node, end=" ")

            # Visit adjacent nodes
            for neighbor in self.graph[node]:

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    # Recursive DFS Utility Function
    def dfs_recursive(self, node, visited):

        visited.add(node)

        print(node, end=" ")

        # Visit all adjacent vertices recursively
        for neighbor in self.graph[node]:

            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    # Depth First Search (DFS)
    def dfs(self, start):

        visited = set()

        print("\nDFS Traversal:")

        self.dfs_recursive(start, visited)


# Driver Code

# Create graph object
g = Graph()

# Add edges
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('D', 'F')

# Perform BFS
g.bfs('A')

# Perform DFS
g.dfs('A')