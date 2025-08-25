# Number of nodes
n = 5

# Example graph represented as adjacency list
# Each entry: adj[node] = list of (neighbor, weight)
adj = [
    [(1, 2), (3, 6)],          # edges from node 0
    [(0, 2), (2, 3), (3, 8), (4, 5)],  # edges from node 1
    [(1, 3), (4, 7)],          # edges from node 2
    [(0, 6), (1, 8), (4, 9)],  # edges from node 3
    [(1, 5), (2, 7), (3, 9)]   # edges from node 4
]

visited = [False] * n
key = [float('inf')] * n
key[0] = a  # Start from node 0
total_cost = 0

for _ in range(n):
    u = -1
    for i in range(n):
        if not visited[i] and (u == -1 or key[i] < key[u]):
            u = i
    visited[u] = True
    total_cost += key[u]
    for v, w in adj[u]:
        if not visited[v] and w < key[v]:
            key[v] = w

print("Minimum Spanning Tree cost:", total_cost)
