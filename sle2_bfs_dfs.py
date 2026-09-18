from collections import deque
import time

# Same graph for both algorithms
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# BFS
def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    nodes = 0

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        nodes += 1

        if node == goal:
            return nodes

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    return nodes


# DFS
def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    nodes = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes += 1

        if node == goal:
            return nodes

        for neighbour in graph[node]:
            if neighbour not in visited:
                stack.append(neighbour)

    return nodes


# Run BFS
start_time = time.perf_counter()
bfs_nodes = bfs(graph, 'A', 'G')
bfs_time = (time.perf_counter() - start_time) * 1000


# Run DFS
start_time = time.perf_counter()
dfs_nodes = dfs(graph, 'A', 'G')
dfs_time = (time.perf_counter() - start_time) * 1000


# Results
print("BFS vs DFS Performance Analysis")
print("--------------------------------")
print(f"BFS Time: {bfs_time:.4f} ms")
print(f"BFS Nodes Expanded: {bfs_nodes}")

print()

print(f"DFS Time: {dfs_time:.4f} ms")
print(f"DFS Nodes Expanded: {dfs_nodes}")