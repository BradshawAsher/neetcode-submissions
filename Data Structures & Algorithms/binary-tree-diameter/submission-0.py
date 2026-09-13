# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            if not node:
                return 0

            #Compute the height of the left and right subtree
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            #1. Update the max diameter seen so far (number of edges)
            max_diameter = max(max_diameter, left_height + right_height)

            #2. return the height of this node to its parent
            return 1 + max(left_height, right_height)

        dfs(root)
        return max_diameter




