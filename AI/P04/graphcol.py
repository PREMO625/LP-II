# Graph Coloring Problem using Backtracking

# Number of vertices
V = 4

# Number of colors
m = 3

# Graph represented using adjacency matrix
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

# Store colors assigned to vertices
colors = [0] * V


# Function to check whether current color assignment is safe
def is_safe(vertex, color):

    for i in range(V):

        # Adjacent vertices cannot have same color
        if graph[vertex][i] == 1 and colors[i] == color:
            return False

    return True


# Backtracking function
def graph_coloring(vertex):

    # All vertices colored
    if vertex == V:
        return True

    # Try all colors
    for color in range(1, m + 1):

        # Check safe coloring
        if is_safe(vertex, color):

            # Assign color
            colors[vertex] = color

            # Recur for next vertex
            if graph_coloring(vertex + 1):
                return True

            # Backtracking step
            colors[vertex] = 0

    return False


# Driver Code
if graph_coloring(0):

    print("Color Assignment:")

    for i in range(V):
        print("Vertex", i, "-> Color", colors[i])

else:
    print("Solution does not exist")