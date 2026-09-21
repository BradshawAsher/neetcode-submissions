
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int) -> bool:
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False #Cycle detected
            parent[root_x] = root_y
            return True
        
        for u, v in edges:
            if not union(u, v):
                return False
        
        return True



