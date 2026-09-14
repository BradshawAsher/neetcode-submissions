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

        #Map: original Node -> cloned Node (serves as visited tracking too)
        clones = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                #if the neighbor hasn't been cloned yet, create it and enqueue
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                #connect the cloned neighbor to the cloned curr
                clones[curr].neighbors.append((clones[neighbor]))
        
        return clones[node]


        