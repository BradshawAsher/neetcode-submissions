# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #left and right subtree of every node differ in height by no more than 1
        def check_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            #1. check the left subtree
            left_height = check_height(node.left)
            if left_height == -1:
                return -1 # left subtree is unbalanced; propogate failure up immediately
            #2. check the right subtree
            right_height = check_height(node.right)
            if right_height == -1:
                return -1 #right subtree is unbalanced; propogate failure up immediately
            #3. check current node balance
            if abs(left_height - right_height) > 1:
                return -1 #current node is unbalanced

            #4. if balanced, return the actual height of this node
            return 1 + max(left_height, right_height)
        return check_height(root) != -1
            
        