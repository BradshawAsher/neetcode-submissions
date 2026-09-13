# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #essentially flip the tree by mirroring it
        #probably a recursion here

        #base case
        if not root:
            return None
        
        #recursive case
        #can we use a temp var and then go down every time
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)



        #return 
        return root
        