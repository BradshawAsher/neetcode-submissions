# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            #1. Go as far left as possible (to the smallest elements)
            while curr:
                stack.append(curr)
                curr = curr.left

            #2. Pop the current smallest unvisited element
            curr = stack.pop()
            k -= 1

            #3. If k hits 0, you've found the kth smallest
            if k == 0:
                return curr.val

            #4. Move to the right subtree to check larger elements
            curr = curr.right

        