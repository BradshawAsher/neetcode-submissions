# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None

        def inorder(node: Optional[TreeNode]):
            nonlocal k, ans
            if not node or ans is not None:
                return

            #Traverse left (smaller values)
            inorder(node.left)

            #Process current node
            k -= 1
            if k == 0:
                ans = node.val
                return

            #Traverse right (larger values)
            inorder(node.right)

        inorder(root)
        return ans

        