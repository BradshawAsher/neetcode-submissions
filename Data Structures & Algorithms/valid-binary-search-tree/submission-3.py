# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True

            #The current node must strictly satisfy low < val < high
            if not (low < node.val < high):
                return False

            #Left subtree values must be < node.val
            #Right subtree values must be  > node.val
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        return validate(root, float("-inf"), float("inf"))