n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))

# Initialize adjacency list for n nodes
adj = [[] for _ in range(n)]

print("Enter edges (u v):")
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)  # If undirected graph

visited = [False] * n

def dfs(u):
    visited[u] = True
    print(u, end=' ')
    for v in adj[u]:
        if not visited[v]:
            dfs(v)

start = int(input("Enter start node for DFS: "))
dfs(start)
print()
