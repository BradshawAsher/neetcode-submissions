from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n-1:
            return False

        adj = {i: [] for i in range(n)}
        
        #first create the adj map
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        #BFS from node 0 (nodes are 0 to n-1, so node 0 always exists)
        visited = set()
        queue = deque([0])
        visited.add(0)

        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return len(visited) == n



