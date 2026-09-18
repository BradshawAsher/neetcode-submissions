# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #as good or better than O(h) time and O(h) space, where h is the height of the tree
        curr = root

        while curr:
            #If both p and q are smaller, LCA must be in the left subtree
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            
            #If both p and q are larger, LCA must be in the right subtree
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right

            #Otherwise, this is the split point (or one equals curr), making curr the LCA
            else:
                return curr

        