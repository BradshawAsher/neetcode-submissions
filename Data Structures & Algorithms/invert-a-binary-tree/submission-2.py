# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #essentially flip the tree by mirroring it
        #probably a recursion here
        #layer level traversal
        if not root:
            return None

        #1. store the inverted left subtree in a temp var
        inverted_left = self.invertTree(root.left)
        
        #2. store the inverted right subtree
        inverted_right = self.invertTree(root.right)

        #re-assign them swapped
        root.left = inverted_right
        root.right = inverted_left

        return root
        