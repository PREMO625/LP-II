# Prim's Minimum Spanning Tree Algorithm
# Implemented using Greedy Approach

# Number of vertices
vertices = 5

# Graph represented using adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Track visited vertices
selected = [False] * vertices

# Start from vertex 0
selected[1] = True

# Number of edges selected
edges = 0

# Store total minimum cost
minimum_cost = 0

print("Edges in Minimum Spanning Tree:\n")

# MST contains (V - 1) edges
while edges < vertices - 1:

    minimum = 9999
    x = 0
    y = 0

    # Traverse all selected vertices
    for i in range(vertices):

        if selected[i]:

            # Check all adjacent vertices
            for j in range(vertices):

                # Select minimum edge
                if not selected[j] and graph[i][j]:

                    if minimum > graph[i][j]:

                        minimum = graph[i][j]
                        x = i
                        y = j

    # Print selected edge
    print(f"{x} - {y} : {graph[x][y]}")

    # Add weight to total cost
    minimum_cost += graph[x][y]

    # Mark new vertex as selected
    selected[y] = True

    # Increment edge count
    edges += 1

# Print final minimum cost
print("\nMinimum Cost =", minimum_cost)