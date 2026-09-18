# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return

            #If we reach a new depth level for the first time, create a bucket for it
            if len(res) == depth:
                res.append([])
            
            #add the current node's value to its corresponding level list
            res[depth].append(node.val)

            #Traverse left then right to preserve left-to-right-order
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 0)
        return res


        