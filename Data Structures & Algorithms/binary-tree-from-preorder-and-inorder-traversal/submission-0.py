# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]: 
        #well this is actually a binary search tree or no?
        #O(n) time and O(n) space
        
        #Map each value to its index in order for O(1) lookup
        inorder_idx_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            nonlocal pre_idx

            #Base case: no elements in this subtree
            if in_left > in_right:
                return None

            #1. The current root is the element at pre_idx
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            #2. Find root's position in inorder
            mid = inorder_idx_map[root_val]

            #3. Build subtrees
            #Left subtree MUST be built first because preorder is [Root, Left, Right]
            root.left = helper(in_left, mid - 1)
            root.right = helper(mid+1, in_right)

            return root

        return helper(0, len(inorder) - 1)
