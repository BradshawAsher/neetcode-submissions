from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #no cycles
        #must be fully connected

        #must have n-1 edges

        #Either have to make sure edges = n-1 and 
        #fully connected (verify all nodes are visited)
        #acyclic (use union-find where no two nodes in an edge already share the same root, or slow-fast)
        #undirected edges
        if len(edges) != n-1:
            return False


        adj = defaultdict(list)
        
        #first create the adj map
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        #BFS from node 0 (nodes are 0 to n-1, so node 0 always exists)
        visited = {0}
        queue = deque([0])
        while queue:
            node = queue.popleft()

            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return len(visited) == n





        #essentially need to do bfs/dfs with visited set to see if there are any disconnected components OR repeats
        #would require first creating an adjacency map


