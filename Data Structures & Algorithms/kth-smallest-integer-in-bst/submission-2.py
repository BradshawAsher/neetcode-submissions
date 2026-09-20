# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        ans = None

        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    ans = curr.val
                curr = curr.right
            else:
                #Find the predecessor (rightmost node in left subtree)
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if not pred.right:
                    #Create temporary thread back to current node
                    pred.right = curr
                    curr = curr.left

                else:
                    #Thread already exists; restore tree structure
                    pred.right = None
                    k -= 1
                    if k == 0:
                        ans = curr.val
                    curr = curr.right

        return ans

        