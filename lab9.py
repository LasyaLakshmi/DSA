def create_graph(edges):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)  # Undirected graph
    return graph

def dfs(graph, start):
    visited = set()
    traversal = []

    def dfs_recursive(node):
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            for neighbor in graph[node]:
                dfs_recursive(neighbor)

    dfs_recursive(start)
    return traversal

def bfs(graph, start):
    visited = set([start])
    queue = [start]
    traversal = []

    while queue:
        node = queue.pop(0)
        traversal.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return traversal
# Taking user input for nodes and edges
nodes = input("Enter nodes separated by space (e.g. A B C D): ").split()
num_edges = int(input("Enter number of edges: "))

edges = []
print("Enter edges in format 'U V' (e.g. A B):")
for _ in range(num_edges):
    u, v = input().split()
    edges.append((u, v))

graph = create_graph(edges)
print("\nGraph adjacency list:")
for node in graph:
    print(f"{node}: {graph[node]}")

start_node = input("\nEnter the starting node for DFS and BFS: ")
dfs_traversal = dfs(graph, start_node)

print("DFS Traversal starting from", start_node, ":", dfs_traversal)
bfs_traversal = bfs(graph, start_node)
print("BFS Traversal starting from", start_node, ":", bfs_traversal)
print("Tejaswini-24303")
