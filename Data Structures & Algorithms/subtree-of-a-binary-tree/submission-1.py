# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #essentially check for occurrences of the subRoot root in the original tree and then see if it works (same tree)
    #first do a regular iteration of root, first root, then root.left, then root.right (in-order???)

        #an empty tree is a subtree of anything
        if not subRoot:
            return True

        #if the main tree is exhausted by subRoot is not, it can't be a subtree
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        #otherwise, check left or right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #if both are none
        if not p and not q:
            return True
        
        #if one is none
        if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        