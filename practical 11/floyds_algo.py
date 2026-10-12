# Floyd-Warshall Algorithm (All-Pairs Shortest Path)
# Using Dynamic Programming

INF = float('inf')


def floyd_warshall(graph):
    """
    Computes the shortest distances between every pair of vertices.
    graph: 2D list where graph[i][j] is the weight of edge from i to j,
           0 if i == j, and INF if there is no edge.
    """
    V = len(graph)

    # Initialize distance matrix same as the input graph matrix
    dist = [row[:] for row in graph]

    # Add all vertices one by one to the set of intermediate vertices
    for k in range(V):
        # Pick all vertices as source one by one
        for i in range(V):
            # Pick all vertices as destination for the above picked source
            for j in range(V):
                # If vertex k is on the shortest path from i to j,
                # then update the value of dist[i][j]
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def print_solution(dist):
    """Utility function to print the shortest distance matrix."""
    V = len(dist)
    print("\nShortest distance matrix between every pair of vertices:\n")
    print("     ", end="")
    for i in range(V):
        print(f"[{i}]".rjust(7), end="")
    print()
    print("-" * (7 * V + 6))

    for i in range(V):
        print(f"[{i}]|", end="")
        for j in range(V):
            if dist[i][j] == INF:
                print("INF".rjust(7), end="")
            else:
                print(str(dist[i][j]).rjust(7), end="")
        print()


if __name__ == '__main__':
    # Number of vertices: 4
    # INF represents no direct edge
    graph = [
        [0, 3, INF, 7],
        [8, 0, 2, INF],
        [5, INF, 0, 1],
        [2, INF, INF, 0]
    ]

    print("=" * 45)
    print("   FLOYD-WARSHALL ALGORITHM (ALL PAIRS)")
    print("=" * 45)

    shortest_distances = floyd_warshall(graph)
    print_solution(shortest_distances)
    print("=" * 45)
