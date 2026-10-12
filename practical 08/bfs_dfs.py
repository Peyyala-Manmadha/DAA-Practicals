from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    traversal = []

    while queue:
        vertex = queue.popleft()
        traversal.append(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal


def dfs(graph, start, visited=None, traversal=None):
    if visited is None:
        visited = set()
    if traversal is None:
        traversal = []

    visited.add(start)
    traversal.append(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, traversal)

    return traversal


print("=" * 50)
print("GRAPH SEARCHING - BFS AND DFS")
print("=" * 50)

n_vertices = int(input("Enter number of vertices: "))
vertices = []
for i in range(n_vertices):
    v = input(f"Enter vertex {i + 1}: ")
    vertices.append(v)

graph = {v: [] for v in vertices}

n_edges = int(input("\nEnter number of edges: "))
print("Enter edges (source destination):")
for i in range(n_edges):
    u, v = input(f"Edge {i + 1}: ").split()
    graph[u].append(v)
    graph[v].append(u)

start_node = input("\nEnter starting vertex for traversal: ")

bfs_result = bfs(graph, start_node)
dfs_result = dfs(graph, start_node)

print("\n" + "=" * 50)
print("RESULTS")
print("=" * 50)
print("BFS Traversal:", bfs_result)
print("DFS Traversal:", dfs_result)

print("\nTime Complexity:")
print("BFS : O(V + E)")
print("DFS : O(V + E)")

print("\nSpace Complexity:")
print("BFS : O(V)")
print("DFS : O(V)")
print("=" * 50)
