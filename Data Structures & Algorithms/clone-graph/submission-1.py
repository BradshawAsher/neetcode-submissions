"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #literally just build an adjacency list with a dict?
        if not node:
            return None
        
        clones = {}

        def dfs(curr: 'Node') -> 'Node':
            if curr in clones:
                return clones[curr]
            
            copy = Node(curr.val)
            clones[curr] = copy

            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy

        
        return dfs(node)


        