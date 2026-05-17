# Graph with weights
graph = {
    'A': [('B', 1), ('C', 5)],
    'B': [('D', 7)],
    'C': [('D', 10)],
    'D': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 0
}

# A* Algorithm
def astar(start, goal):

    # Open list stores nodes to explore
    open_list = [start]

    # Store visited nodes
    closed_list = []

    # Actual cost from source
    g_cost = {
        start: 0
    }

    # Parent nodes for path
    parent = {
        start: start
    }

    while open_list:

        # Find node with minimum f(n)
        current = open_list[0]

        for node in open_list:

            f_current = g_cost[current] + heuristic[current]
            f_node = g_cost[node] + heuristic[node]

            if f_node < f_current:
                current = node

        # Goal reached
        if current == goal:

            path = []

            while parent[current] != current:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            return path

        # Remove current from open list
        open_list.remove(current)

        # Add to closed list
        closed_list.append(current)

        # Explore neighbors
        for neighbor, weight in graph[current]:

            if neighbor not in open_list and neighbor not in closed_list:

                open_list.append(neighbor)

                parent[neighbor] = current

                g_cost[neighbor] = g_cost[current] + weight

    return None


# Driver code
path = astar('A', 'D')

print("Shortest Path :", " -> ".join(path))