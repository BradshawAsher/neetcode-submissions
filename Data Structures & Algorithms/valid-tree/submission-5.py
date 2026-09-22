
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Condition 1: A valid tree with n nodes must have exactly n-1 edges
        if len(edges) != n-1:
            return False

        #Build undirected adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node: int):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        #Start traversal from node 0
        dfs(0)

        #Since E == n-1, checking if all nodes are visited proves it's a valid tree
        return len(visited) == n

